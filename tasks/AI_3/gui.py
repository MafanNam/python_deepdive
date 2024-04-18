from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QWidget, QSlider
from PyQt5.QtCore import Qt
import pyqtgraph as pg
from numpy import arange

from ekg import EKG
from pyqtgraph import PlotWidget


class GUI(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super(GUI, self).__init__(*args, **kwargs)

        self.setWindowIcon(QtGui.QIcon('4.png'))

        self.graphWidget = PlotWidget()
        self.graphWidget.setMinimumSize(QtCore.QSize(600, 500))
        self.graphWidget.showGrid(x=True, y=True)
        self.graphWidget.setLabel('bottom', 'Час (мс)')
        self.graphWidget.setLabel('left', 'Амплітуда (мВ)')

        self.ekg_simulator = EKG()
        self.bit = 70;
        self.__plot_ekg()

        self.__add_a_slider()
        self.__add_m_slider()
        self.__add_b1_slider()
        self.__add_b2_slider()
        self.__add_line()

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.addItem(
            QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
        self.Amp = QtWidgets.QLabel('Амплітуда:')
        self.Amp.setToolTip("Діапазон ( -0.5 : 0.5 ) мВ")

        self.horizontalLayout.addWidget(self.Amp)
        self.horizontalLayout.addItem(
            QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.addItem(
            QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))

        self.Time = QtWidgets.QLabel('Час:')
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

        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.addWidget(self.graphWidget)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout.addWidget(self.a_slider)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addWidget(self.m_slider)
        self.verticalLayout.addWidget(self.b1_slider)
        self.verticalLayout.addWidget(self.b2_slider)

        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.setCentralWidget(QWidget())
        self.centralWidget().setLayout(self.verticalLayout)

        self.setWindowTitle("Lab 3 BS-24 Manzik")

    def __add_a_slider(self):
        self.a_slider = QSlider(Qt.Horizontal, self)
        self.a_slider.setValue(int(self.ekg_simulator.T.A * 100))
        self.a_slider.setMinimum(-50)
        self.a_slider.setMaximum(50)
        self.a_slider.sliderMoved.connect(
            self.__on_a_slider_moved
        )

    def __add_m_slider(self):
        self.m_slider = QSlider(Qt.Horizontal, self)
        self.m_slider.setValue(int(self.ekg_simulator.T.m * 100))
        self.m_slider.setMinimum(70)
        self.m_slider.setMaximum(90)
        self.m_slider.sliderMoved.connect(
            self.__on_m_slider_moved
        )

    def __add_b1_slider(self):
        self.b1_slider = QSlider(Qt.Horizontal, self)
        self.b1_slider.setValue(int(self.ekg_simulator.T.b1 * 1000))
        self.b1_slider.setMinimum(1)
        self.b1_slider.setMaximum(30)
        self.b1_slider.sliderMoved.connect(
            self.__on_b1_slider_moved
        )

    def __add_b2_slider(self):
        self.b2_slider = QSlider(Qt.Horizontal, self)
        self.b2_slider.setValue(int(self.ekg_simulator.T.b2 * 1000))
        self.b2_slider.setMinimum(1)
        self.b2_slider.setMaximum(30)
        self.b2_slider.sliderMoved.connect(
            self.__on_b2_slider_moved
        )

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
        self.Bit_line.setFixedWidth(50)
        self.Bit_line.setValidator(QIntValidator(60, 120))
        self.Bit_line.setText('70')
        self.bit = int(self.Bit_line.text())
        self.Bit_line.returnPressed.connect(
            self.line_change
        )

    def line_change(self):
        self.bit = int(self.Bit_line.text())
        self.__plot_ekg()

    def __plot_ekg(self):
        t0 = int(60 * 1000 / self.bit)
        x_fake = arange(0, 1, 0.001)
        sizz = x_fake.size
        x = arange(0, t0, t0 / (sizz))
        y = [self.ekg_simulator.get(t) for t in x_fake]

        self.graphWidget.setBackground('#21071e')
        self.graphWidget.plot(x, y, clear=True, pen=pg.mkPen(color=('#fad0f2'), width=2))
