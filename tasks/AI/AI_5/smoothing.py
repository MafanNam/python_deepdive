from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QSlider, QVBoxLayout, QLabel, QDesktopWidget, QCheckBox
from PyQt5.QtCore import Qt
import pyqtgraph as pg
from numpy import arange


class SmoothingGui(QtWidgets.QMainWindow):
    def __init__(self, parent):
        super(SmoothingGui, self).__init__(parent)
        self.ekg_simulator = parent.ekg_simulator
        self.step = 0.001
        self.setFixedWidth(int(QDesktopWidget().width() * 0.7))

        self.graphWidget = pg.PlotWidget()
        self.graphWidget.showGrid(x=True, y=True)
        self.graphWidget.setLabel('bottom', 'Час (с)')
        self.graphWidget.setLabel('left', 'Амплітуда (мВ)')

        styles = {'color': '#666', 'font-size': '12px'}
        self.graphWidget.getAxis('bottom').setPen(pg.mkPen(color='#666', width=2))
        self.graphWidget.getAxis('left').setPen(pg.mkPen(color='#666', width=2))

        self.graphWidget.setXRange(0, 4)

        self.__add_a_slider()
        self.__add_w_slider()
        self.__add_checkboxes()

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.graphWidget)
        self.layout.addWidget(self.__add_a_label())
        self.layout.addWidget(self.a_slider)
        self.layout.addWidget(self.__add_w_label())
        self.layout.addWidget(self.w_slider)
        self.layout.addWidget(self.exp_cb)
        self.layout.setAlignment(self.exp_cb, Qt.AlignHCenter)
        self.layout.addWidget(self.avg_cb)
        self.layout.setAlignment(self.avg_cb, Qt.AlignHCenter)

        self.__upd_checkboxes()

        self.__plot_ekg()

        self.setCentralWidget(QWidget())
        self.centralWidget().setLayout(self.layout)
        self.setWindowTitle("Лабораторна 5")

    def __add_a_label(self):
        self.a_label = QLabel(f'Альфа: 0.5')
        return self.a_label

    def __add_w_label(self):
        self.w_label = QLabel(f'Ширина: 2')
        return self.w_label

    def __add_a_slider(self):
        self.a_slider = QSlider(Qt.Horizontal, self)
        self.a_slider.setEnabled(False)
        self.a_slider.setValue(50)
        self.a_slider.setMinimum(1)
        self.a_slider.setMaximum(100)
        self.a_slider.sliderReleased.connect(self.__on_a_slider_released)

    def __add_w_slider(self):
        self.w_slider = QSlider(Qt.Horizontal, self)
        self.w_slider.setEnabled(False)
        self.w_slider.setValue(2)
        self.w_slider.setMinimum(1)
        self.w_slider.setMaximum(30)
        self.w_slider.sliderReleased.connect(self.__on_w_slider_released)

    def __add_checkboxes(self):
        self.exp_cb = QCheckBox('Експоненційне згладжування')
        self.exp_cb.stateChanged.connect(self.__exp_on_change)
        self.avg_cb = QCheckBox('Ковзне середнє')
        self.avg_cb.stateChanged.connect(self.__avg_on_change)

    def __on_a_slider_released(self):
        self.a_label.setText(f'Параметр альфа: {self.a_slider.value() / 100}')
        self.__plot_ekg()

    def __on_w_slider_released(self):
        self.w_label.setText(f'Ширина вікна: {self.w_slider.value()}')
        self.__plot_ekg()

    def __exp_on_change(self):
        if self.exp_cb.isChecked():
            self.avg_cb.setChecked(False)
        self.__upd_checkboxes()

    def __avg_on_change(self):
        if self.avg_cb.isChecked():
            self.exp_cb.setChecked(False)
        self.__upd_checkboxes()

    def __upd_checkboxes(self):
        self.a_slider.setEnabled(self.exp_cb.isChecked())
        if self.avg_cb.isChecked():
            self.w_slider.setEnabled(True)
        self.__plot_ekg()

    def __plot_ekg(self):
        x = arange(0, 5, self.step)
        y = [self.ekg_simulator.get_alternation(t) for t in x]
        if self.exp_cb.isChecked():
            a = self.a_slider.value() / 100
            for i in range(1, len(y)):
                y[i] = a * y[i] + (1 - a) * y[i - 1]
        elif self.avg_cb.isChecked():
            w = self.w_slider.value()
            window = [0] * w
            smoothed = []
            for i in range(len(y)):
                window.pop(0)
                window.append(y[i])
                if i >= w - 1:
                    smoothed.append(sum(window) / w)
            y = smoothed

        self.graphWidget.setBackground('#1111')
        self.graphWidget.plot(x[:len(y)], y, clear=True, pen=pg.mkPen(color=('#000000'), width=2))
