from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QWidget, QSlider, QPushButton
from PyQt5.QtCore import Qt
import pyqtgraph as pg
from numpy import arange
from ekg import EKG
from pyqtgraph import PlotWidget
from generation_gui import GenerationGUI


class GUI(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super(GUI, self).__init__(*args, **kwargs)

        self.graphWidget = PlotWidget()
        self.graphWidget.setMinimumSize(QtCore.QSize(900, 600))

        self.graphWidget.showGrid(x=True, y=True, alpha=0.5)

        # Dark style
        self.graphWidget.setBackground('#222222')
        pg.setConfigOption('foreground', '#DDDDDD')  # Text color

        styles = {'color': '#666', 'font-size': '12px'}
        self.graphWidget.getAxis('bottom').setPen(pg.mkPen(color='black', width=2))
        self.graphWidget.getAxis('left').setPen(pg.mkPen(color='black', width=2))

        self.graphWidget.getAxis('bottom').setLabel(text='Час (с)', **styles)
        self.graphWidget.getAxis('left').setLabel(text='Амплітуда (мВ)', **styles)

        self.ekg_simulator = EKG()
        self.bit = 70
        self.__plot_ekg()

        self.__add_a_slider()
        self.__add_m_slider()
        self.__add_b1_slider()
        self.__add_b2_slider()
        self.__add_line()
        self.__add_button()

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.addItem(
            QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
        self.Amp = QtWidgets.QLabel('Амплітуда')
        self.Amp.setToolTip("Діапазон ( -0.5 : 0.5 ) мВ")

        self.horizontalLayout.addWidget(self.Amp)
        self.horizontalLayout.addItem(
            QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.addItem(
            QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
        self.Time = QtWidgets.QLabel('Час')
        self.Time.setToolTip("Діапазон ( 0.7 : 0.9 ) c")

        self.horizontalLayout_2.addWidget(self.Time)
        self.horizontalLayout_2.addItem(
            QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.addItem(
            QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))

        self.b1b2 = QtWidgets.QLabel('Ширина:')
        self.b1b2.setToolTip("Діапазон ( 0.001 : 0.03 ) ")

        self.horizontalLayout_3.addWidget(self.b1b2)
        self.horizontalLayout_3.addItem(
            QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))

        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.addItem(
            QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
        self.horizontalLayout_4.addWidget(self.Bit_line)
        self.heart_rate_label = QtWidgets.QLabel('Кількість серцевих скорочень')

        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.addItem(
            QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
        self.t1_label = QtWidgets.QLabel('Т1')
        self.t1_label.setToolTip("Діапазон ( 0.001 : 0.03 ) ")

        self.horizontalLayout_5.addWidget(self.t1_label)
        self.horizontalLayout_5.addItem(
            QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))

        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.addItem(
            QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
        self.t2_label = QtWidgets.QLabel('Т2')
        self.t2_label.setToolTip("Діапазон ( 0.001 : 0.03 ) ")

        self.horizontalLayout_6.addWidget(self.t2_label)
        self.horizontalLayout_6.addItem(
            QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))

        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.addWidget(self.graphWidget)
        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_4.addWidget(self.heart_rate_label)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalLayout.addWidget(self.a_slider)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addWidget(self.m_slider)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.verticalLayout.addWidget(self.b1_slider)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.verticalLayout.addWidget(self.b2_slider)
        self.verticalLayout.addWidget(self.generate_button)

        self.setCentralWidget(QWidget())
        self.centralWidget().setLayout(self.verticalLayout)

        self.setWindowTitle("Лабараторна 3")

    def __add_a_slider(self):
        self.a_slider = QSlider(Qt.Horizontal, self)
        self.a_slider.setValue(int(self.ekg_simulator.T.A * 100))
        self.a_slider.setMinimum(-50)
        self.a_slider.setMaximum(50)
        self.a_slider.sliderMoved.connect(self.__on_a_slider_moved)

    def __add_m_slider(self):
        self.m_slider = QSlider(Qt.Horizontal, self)
        self.m_slider.setValue(int(self.ekg_simulator.T.m * 100))
        self.m_slider.setMinimum(70)
        self.m_slider.setMaximum(90)
        self.m_slider.sliderMoved.connect(self.__on_m_slider_moved)

    def __add_b1_slider(self):
        self.b1_slider = QSlider(Qt.Horizontal, self)
        self.b1_slider.setValue(int(self.ekg_simulator.T.b1 * 1000))
        self.b1_slider.setMinimum(1)
        self.b1_slider.setMaximum(30)
        self.b1_slider.sliderMoved.connect(self.__on_b1_slider_moved)

    def __add_b2_slider(self):
        self.b2_slider = QSlider(Qt.Horizontal, self)
        self.b2_slider.setValue(int(self.ekg_simulator.T.b2 * 1000))
        self.b2_slider.setMinimum(1)
        self.b2_slider.setMaximum(30)
        self.b2_slider.sliderMoved.connect(self.__on_b2_slider_moved)

    def __on_a_slider_moved(self):
        self.ekg_simulator.T.A = self.a_slider.value() / 100
        self.__plot_ekg()

    def __on_m_slider_moved(self):
        self.ekg_simulator.T.m = self.m_slider.value() / 100
        self.__plot_ekg()

    def __on_b1_slider_moved(self):
        self.ekg_simulator.T.b1 = self.b1_slider.value() / 1000
        self.__plot_ekg()

    def __on_b2_slider_moved(self):
        self.ekg_simulator.T.b2 = self.b2_slider.value() / 1000
        self.__plot_ekg()

    def __add_line(self):
        self.Bit_line = QtWidgets.QLineEdit()
        self.Bit_line.setFixedWidth(100)
        self.Bit_line.setValidator(QIntValidator(60, 120))
        self.Bit_line.setText('70')
        self.bit = int(self.Bit_line.text())
        self.Bit_line.returnPressed.connect(self.line_change)

    def line_change(self):
        self.bit = int(self.Bit_line.text())
        self.__plot_ekg()

    def generate_ekg(self):
        generation_gui = GenerationGUI(self)
        generation_gui.show()

    def __add_button(self):
        self.generate_button = QPushButton('Генерація', self)
        self.generate_button.clicked.connect(self.generate_ekg)

    def __plot_ekg(self):
        t0 = int(60 * 1000 / self.bit)
        x_fake = arange(0, 1, 0.001)
        sizz = x_fake.size
        x = arange(0, t0 / 1000, t0 / (sizz * 1000))
        y = [self.ekg_simulator.get(t) for t in x_fake]

        self.graphWidget.setBackground('#1111')
        self.graphWidget.plot(x, y, clear=True, pen=pg.mkPen(color=('purple'), width=2))


app = QtWidgets.QApplication([])
window = GUI()
window.show()
app.exec_()
