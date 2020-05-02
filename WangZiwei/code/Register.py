import sys
from PyQt5 import QtCore, QtWidgets, QtGui


class RegisterWindow():
    def Ui_setup(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        # 设置主窗口尺寸
        MainWindow.resize(400, 650)

        # 设置主窗口标题
        MainWindow.setWindowTitle('注册')
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        MainWindow.setCentralWidget(self.centralwidget)

        # 添加label
        self.add_Label(MainWindow)
        # 添加输入框
        self.add_LineEdit(MainWindow)
        # 添加按钮
        self.add_Button(MainWindow)
        # 设置背景
        self.set_Background(MainWindow)


        # 设置布局
        vbox = QtWidgets.QVBoxLayout()
        mainwg = QtWidgets.QWidget()
        mainLayout = QtWidgets.QVBoxLayout()

        namelayout = QtWidgets.QHBoxLayout()
        namelayout.addStretch(1)
        namelayout.addWidget(self.nameLabel)
        namelayout.addWidget(self.nameLineEdit)
        namelayout.addStretch(1)
        namewidget = QtWidgets.QWidget()
        namewidget.setLayout(namelayout)

        passwordlayout = QtWidgets.QHBoxLayout()
        passwordlayout.addStretch(1)
        passwordlayout.addWidget(self.passwordLabel)
        passwordlayout.addWidget(self.passwordLineEdit)
        passwordlayout.addStretch(1)
        passwordwidget = QtWidgets.QWidget()
        passwordwidget.setLayout(passwordlayout)

        confirmlayout = QtWidgets.QHBoxLayout()
        confirmlayout.addStretch(1)
        confirmlayout.addWidget(self.confirmLable)
        confirmlayout.addWidget(self.confirmLineEdit)
        confirmlayout.addStretch(1)
        confirmwidget = QtWidgets.QWidget()
        confirmwidget.setLayout(confirmlayout)

        mainLayout.addWidget(namewidget)
        mainLayout.addWidget(passwordwidget)
        mainLayout.addWidget(confirmwidget)

        btnlayout = QtWidgets.QHBoxLayout()
        btnlayout.addStretch(1)
        btnlayout.addWidget(self.btnSign)
        btnlayout.addWidget(self.btnReturn)
        btnlayout.addStretch(1)

        btnwg = QtWidgets.QWidget()
        btnwg.setLayout(btnlayout)


        mainwg.setLayout(mainLayout)
        vbox.addStretch(1)
        vbox.addWidget(mainwg)
        vbox.addWidget(btnwg)
        vbox.addStretch(2)

        self.centralwidget.setLayout(vbox)


    def set_Background(self, MainWindow):
        # 设置背景
        palette = QtGui.QPalette()
        pix = QtGui.QPixmap('/home/wangziwei/Pictures/1.jpg').scaled(MainWindow.width(), MainWindow.height())
        palette.setBrush(QtGui.QPalette.Background, QtGui.QBrush(pix))
        MainWindow.setPalette(palette)

    def add_Label(self, MainWindow):
        # 用户名,密码,确认密码
        self.nameLabel = QtWidgets.QLabel('&Name:     ')
        self.passwordLabel = QtWidgets.QLabel('&Password:')
        self.confirmLable = QtWidgets.QLabel('&Confirmed:')

    def add_LineEdit(self, MainWindow):
        self.nameLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.nameLineEdit.setPlaceholderText('username')
        self.nameLineEdit.setStyleSheet('background: rgb(255, 255, 255, 100)')

        self.passwordLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.passwordLineEdit.setPlaceholderText('password')
        self.passwordLineEdit.setStyleSheet('background: rgb(255, 255, 255, 100)')
        self.passwordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)

        self.confirmLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.confirmLineEdit.setPlaceholderText('password again')
        self.confirmLineEdit.setStyleSheet('background: rgb(255, 255, 255, 100)')
        self.confirmLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)

        # 设置伙伴控件
        self.nameLabel.setBuddy(self.nameLineEdit)
        self.passwordLabel.setBuddy(self.passwordLineEdit)
        self.confirmLable.setBuddy(self.confirmLineEdit)

    def add_Button(self, MainWindow):
        op = QtWidgets.QGraphicsOpacityEffect()
        op.setOpacity(0.8)
        self.btnSign = QtWidgets.QPushButton('Sign Up')
        self.btnSign.setGraphicsEffect(op)
        self.btnSign.setStyleSheet('background-color:blue')

        self.btnReturn = QtWidgets.QPushButton('Return')
        self.btnReturn.setGraphicsEffect(op)
        self.btnReturn.setStyleSheet('background-color:blue')






