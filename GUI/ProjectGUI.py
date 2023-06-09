from PyQt5 import QtCore, QtGui, QtWidgets

from Classes import Project, Employee, LinkedList

# This class was build in PyQtDesigner
# GUI code using PyQt5
class Ui_MainWindow(object):
    # initialize variables
    employee_lst = []
    projects = LinkedList()

    # adds employee from input data
    def add_employee(self):
        index = self.project_list.currentRow()
        temp = self.project_list.takeItem(index)
        temp2 = Employee(self.employee_name.text(), temp.text())
        self.employee_lst.append(temp2)
        self.tableWidget_2.addItem(str(temp2))

    # add project
    def add_project(self):
        temp_date = self.dateEdit.date()
        date_object = temp_date.toPyDate()
        temp = Project(self.project_name.text(), date_object, self.project_description.toPlainText())
        self.projects.insert(temp)
        self.project_list2.addItem(str(temp))
        self.dateEdit.clear()
        self.project_name.clear()
        self.project_description.clear()
        self.project_list.addItem(str(temp))

    # builds the GUI based on information from PyQtDesigner
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(857, 650)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-1, -1, 801, 541))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 81, 541))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")

        # set button action - when clicked set current screen
        self.btn_add_proj = QtWidgets.QPushButton(self.frame_2, clicked = lambda: self.stackedWidget.setCurrentWidget(self.add_projects))
        self.btn_add_proj.setGeometry(QtCore.QRect(0, 0, 81, 41))
        self.btn_add_proj.setObjectName("btn_add_proj")

        # set button action - when clicked set current screen
        self.bton_add_emp = QtWidgets.QPushButton(self.frame_2, clicked = lambda: self.stackedWidget.setCurrentWidget(self.add_employees))
        self.bton_add_emp.setGeometry(QtCore.QRect(0, 40, 81, 41))
        self.bton_add_emp.setObjectName("bton_add_emp")

        # set button action - when clicked set current screen
        self.bton_view_proj = QtWidgets.QPushButton(self.frame_2, clicked = lambda: self.stackedWidget.setCurrentWidget(self.view_projects))
        self.bton_view_proj.setGeometry(QtCore.QRect(0, 80, 81, 41))
        self.bton_view_proj.setObjectName("bton_view_proj")

        # set button action - when clicked set current screen
        self.bton_view_emp = QtWidgets.QPushButton(self.frame_2, clicked = lambda: self.stackedWidget.setCurrentWidget(self.view_employees))
        self.bton_view_emp.setGeometry(QtCore.QRect(0, 120, 81, 41))
        self.bton_view_emp.setObjectName("bton_view_emp")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setGeometry(QtCore.QRect(80, 0, 721, 541))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_3)
        self.stackedWidget.setObjectName("stackedWidget")
        self.add_employees = QtWidgets.QWidget()
        self.add_employees.setObjectName("add_employees")
        self.QVBoxLayout = QtWidgets.QVBoxLayout(self.add_employees)
        self.QVBoxLayout.setObjectName("QVBoxLayout")
        self.label_instruction = QtWidgets.QLabel(self.add_employees)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(18)
        self.label_instruction.setFont(font)
        self.label_instruction.setObjectName("label_instruction")
        self.QVBoxLayout.addWidget(self.label_instruction)
        self.label_date = QtWidgets.QLabel(self.add_employees)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        self.label_date.setFont(font)
        self.label_date.setObjectName("label_date")
        self.QVBoxLayout.addWidget(self.label_date)
        self.employee_name = QtWidgets.QLineEdit(self.add_employees)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(10)
        self.employee_name.setFont(font)
        self.employee_name.setText("")
        self.employee_name.setObjectName("employee_name")
        self.QVBoxLayout.addWidget(self.employee_name)
        self.label = QtWidgets.QLabel(self.add_employees)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.QVBoxLayout.addWidget(self.label)
        self.project_list = QtWidgets.QListWidget(self.add_employees)
        self.project_list.setObjectName("project_list")

        # adds all items from LinkedList projects to project_list GUI
        a = iter(self.projects)
        while True:
            try:
                curr = a.__next__()
                self.project_list.addItem(str(curr))
            except StopIteration:
                break
        self.QVBoxLayout.addWidget(self.project_list)

        # set button action - when clicked calls add_employee method
        self.pushButton_2 = QtWidgets.QPushButton(self.add_employees, clicked = lambda: self.add_employee())
        self.pushButton_2.setObjectName("pushButton_2")
        self.QVBoxLayout.addWidget(self.pushButton_2)
        self.add_projects = QtWidgets.QWidget()
        self.add_projects.setObjectName("add_projects")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.add_projects)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_4 = QtWidgets.QFrame(self.add_projects)
        self.frame_4.setMaximumSize(QtCore.QSize(427, 16777215))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_instruction_2 = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(18)
        self.label_instruction_2.setFont(font)
        self.label_instruction_2.setObjectName("label_instruction_2")
        self.gridLayout_2.addWidget(self.label_instruction_2, 0, 0, 1, 3)
        self.project_name = QtWidgets.QLineEdit(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(10)
        self.project_name.setFont(font)
        self.project_name.setText("")
        self.project_name.setObjectName("project_name")
        self.gridLayout_2.addWidget(self.project_name, 1, 0, 1, 1)
        self.label_date_2 = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(18)
        self.label_date_2.setFont(font)
        self.label_date_2.setObjectName("label_date_2")
        self.gridLayout_2.addWidget(self.label_date_2, 1, 1, 1, 1)
        self.dateEdit = QtWidgets.QDateEdit(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(10)
        self.dateEdit.setFont(font)
        self.dateEdit.setObjectName("dateEdit")
        self.gridLayout_2.addWidget(self.dateEdit, 1, 2, 1, 1)
        self.verticalLayout_4.addWidget(self.frame_4)
        self.project_description = QtWidgets.QTextEdit(self.add_projects)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(10)
        self.project_description.setFont(font)
        self.project_description.setObjectName("project_description")
        self.verticalLayout_4.addWidget(self.project_description)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(10)

        # set button action - when clicked calls add_project method
        self.pushButton = QtWidgets.QPushButton(self.add_projects, clicked=lambda: self.add_project())
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_4.addWidget(self.pushButton)
        self.stackedWidget.addWidget(self.add_projects)
        self.stackedWidget.addWidget(self.add_employees)
        self.view_projects = QtWidgets.QWidget()
        self.view_projects.setObjectName("view_projects")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.view_projects)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.view_projects)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(24)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.project_list2 = QtWidgets.QListWidget(self.view_projects)
        self.project_list2.setObjectName("tableWidget")

        # adds all items from LinkedList projects to project_list2 GUI
        a = iter(self.projects)
        while True:
            try:
                curr = a.__next__()
                self.project_list2.addItem(str(curr))
            except StopIteration:
                break
        self.verticalLayout_2.addWidget(self.project_list2)

        self.stackedWidget.addWidget(self.view_projects)
        self.view_employees = QtWidgets.QWidget()
        self.view_employees.setObjectName("view_employees")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.view_employees)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.view_employees)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(24)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.tableWidget_2 = QtWidgets.QListWidget(self.view_employees)
        self.tableWidget_2.setObjectName("tableWidget_2")

        # adds all employees to employee list GUI
        for ele in self.employee_lst:
            self.tableWidget_2.addItem(str(ele))

        self.verticalLayout_3.addWidget(self.tableWidget_2)
        self.stackedWidget.addWidget(self.view_employees)
        self.verticalLayout.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 857, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_add_proj.setText(_translate("MainWindow", "Add Projects"))
        self.bton_add_emp.setText(_translate("MainWindow", "Add Employees"))
        self.bton_view_proj.setText(_translate("MainWindow", "View Projects"))
        self.bton_view_emp.setText(_translate("MainWindow", "View Employees"))
        self.label_instruction.setText(_translate("MainWindow", "Enter Employee name and assign projects"))
        self.label_date.setText(_translate("MainWindow", "Employee Name:"))
        self.employee_name.setPlaceholderText(_translate("MainWindow", "Name"))
        self.label.setText(_translate("MainWindow", "Assign Projects"))
        self.pushButton_2.setText(_translate("MainWindow", "Add Employee"))
        self.label_instruction_2.setText(_translate("MainWindow", "Enter your project names and Dates"))
        self.project_name.setPlaceholderText(_translate("MainWindow", "Projcet Name"))
        self.label_date_2.setText(_translate("MainWindow", "Date:"))
        self.project_description.setPlaceholderText(_translate("MainWindow", "Description"))
        self.pushButton.setText(_translate("MainWindow", "Add Project"))
        self.label_3.setText(_translate("MainWindow", "Project List - By Date"))
        self.label_4.setText(_translate("MainWindow", "Employee List"))
