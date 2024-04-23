from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import (
    QWidget,
    QSlider,
    QVBoxLayout,
    QLabel,
)
from PyQt5.QtCore import Qt
from pyqtgraph import PlotWidget
import pyqtgraph as pg
from numpy import arange


class GenerationGUI(QtWidgets.QMainWindow):
    def __init__(self, parent):
        super(GenerationGUI, self).__init__(parent)
        self.ekg_simulator = parent.ekg_simulator
        self.step = 0.002

        self.graphWidget = PlotWidget()
        self.graphWidget.setMinimumSize(QtCore.QSize(900, 400))
        self.graphWidget.showGrid(x=True, y=True)
        self.graphWidget.setLabel('bottom', 'Час (с)')
        self.graphWidget.setLabel('left', 'Амплітуда (мВ)')
        self.graphWidget.setXRange(0, 4)

        self.__add_m_slider()
        self.__add_l_slider()
        self.__add_h_slider()

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.graphWidget)
        label1 = self.__add_label()
        self.layout.addWidget(label1)
        self.layout.setAlignment(label1, Qt.AlignHCenter)
        self.layout.addWidget(self.m_slider)
        label2 = QLabel('Альтернація:')
        self.layout.addWidget(label2)
        self.layout.setAlignment(label2, Qt.AlignHCenter)
        self.layout.addWidget(self.l_slider)
        self.layout.addWidget(QLabel('Шум:'), 0, Qt.AlignHCenter)
        self.layout.addWidget(self.h_slider)

        self.__plot_ekg()

        self.setCentralWidget(QWidget())
        self.centralWidget().setLayout(self.layout)
        self.setWindowTitle("Lab 4")

    def __add_label(self):
        self.label = QLabel(f'Цикли: {self.m_slider.value()}')
        return self.label

    def __add_m_slider(self):
        self.m_slider = QSlider(Qt.Horizontal, self)
        self.m_slider.setValue(30)
        self.m_slider.setMinimum(1)
        self.m_slider.setMaximum(50)
        self.m_slider.sliderMoved.connect(
            self.__on_m_slider_moved
        )

    def __add_l_slider(self):
        self.l_slider = QSlider(Qt.Horizontal, self)
        self.l_slider.setValue(0)
        self.l_slider.setMinimum(0)
        self.l_slider.setMaximum(100)
        self.l_slider.sliderReleased.connect(
            self.__on_l_slider_released
        )

    def __add_h_slider(self):
        self.h_slider = QSlider(Qt.Horizontal, self)
        self.h_slider.setValue(int(self.ekg_simulator.h * 100))
        self.h_slider.setMinimum(0)
        self.h_slider.setMaximum(100)
        self.h_slider.sliderReleased.connect(
            self.__plot_ekg
        )

    def __on_m_slider_moved(self):
        self.label.setText(f'Цикли: {self.m_slider.value()}')
        self.__plot_ekg()

    def __on_l_slider_released(self):
        self.ekg_simulator.T._lambda = 1 + self.l_slider.value() / 100
        self.__plot_ekg()

    def __plot_ekg(self):
        self.ekg_simulator.h = self.h_slider.value() / 100

        bit = 60
        t0 = int(60 * 1000 / bit * self.m_slider.value())
        x_fake = arange(0, self.m_slider.value(), self.step)
        sizz = x_fake.size
        x = arange(0, t0, t0 / (sizz)) / 1000

        y = [self.ekg_simulator.get_alternation(t) for t in x_fake]

        self.graphWidget.setBackground('#21071e')
        self.graphWidget.plot(x, y, clear=True, pen=pg.mkPen(color=('#fad0f2'), width=1.5))
