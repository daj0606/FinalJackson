import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from GUI.ProjectGUI import Ui_MainWindow

# Main
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
