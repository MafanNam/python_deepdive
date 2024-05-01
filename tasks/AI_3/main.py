from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QFile
import sys

from gui import GUI


def main():
    app = QtWidgets.QApplication(sys.argv)
    file = QFile("style.qss")
    if not file.open(QFile.ReadOnly | QFile.Text):
        return
    qss = QtCore.QTextStream(file)
    app.setStyleSheet(qss.readAll())
    main = GUI()
    main.resize(900, 900)
    main.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
