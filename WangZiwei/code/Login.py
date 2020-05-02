from PyQt5 import QtCore, QtWidgets, QtGui

class UiMainWindow():
    def Ui_setup(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        #设置主窗口尺寸
        MainWindow.resize(400, 650)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        MainWindow.setCentralWidget(self.centralwidget)

        #添加label
        self.add_Label(MainWindow)
        #添加输入框
        self.add_LineEdit(MainWindow)
        #添加按钮
        self.add_Button(MainWindow)
        #设置背景
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

        mainLayout.addWidget(namewidget)
        mainLayout.addWidget(passwordwidget)

        btnlayout = QtWidgets.QHBoxLayout()
        btnlayout.addStretch(1)
        btnlayout.addWidget(self.btnOK)
        btnlayout.addStretch(1)

        btnwg = QtWidgets.QWidget()
        btnwg.setLayout(btnlayout)

        textlayout = QtWidgets.QHBoxLayout()
        textlayout.addStretch(1)
        textlayout.addWidget(self.label1)
        textlayout.addStretch(1)
        textlayout.addWidget(self.label2)
        textlayout.addStretch(1)
        textwg = QtWidgets.QWidget()
        textwg.setLayout(textlayout)

        mainwg.setLayout(mainLayout)
        vbox.addStretch(1)
        vbox.addWidget(mainwg)
        vbox.addWidget(btnwg)
        vbox.addWidget(textwg)
        vbox.addStretch(2)

        self.centralwidget.setLayout(vbox)


    def set_Background(self, MainWindow):
        # 设置背景
        palette = QtGui.QPalette()
        pix = QtGui.QPixmap('/home/wangziwei/Pictures/1.jpg').scaled(MainWindow.width(), MainWindow.height())
        palette.setBrush(QtGui.QPalette.Background, QtGui.QBrush(pix))
        MainWindow.setPalette(palette)

    def add_Label(self, MainWindow):
        #用户名密码
        self.nameLabel = QtWidgets.QLabel('&Name:')
        self.passwordLabel = QtWidgets.QLabel('&Password:')


        # 注册，忘记密码
        self.label1 = QtWidgets.QLabel('<style> a {text-decoration: none; color: #999999} </style><a href = "#">新用户注册</a>')
        self.label2 = QtWidgets.QLabel("<style> a {text-decoration: none; color: #999999} </style><a href = '#'>个人信息修改</a>")

    def add_LineEdit(self, MainWindow):
        self.nameLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.nameLineEdit.setPlaceholderText('username')
        self.nameLineEdit.setStyleSheet('background:rgb(255,255,255,100)')

        self.passwordLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.passwordLineEdit.setPlaceholderText('password')
        self.passwordLineEdit.setStyleSheet('background:rgb(255,255,255,100)')
        self.passwordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)

        # 设置伙伴控件
        self.nameLabel.setBuddy(self.nameLineEdit)
        self.passwordLabel.setBuddy(self.passwordLineEdit)

    def add_Button(self,MainWindow):
        op = QtWidgets.QGraphicsOpacityEffect()
        self.btnOK = QtWidgets.QPushButton('                        登录                           ')
        op.setOpacity(0.8)
        self.btnOK.setGraphicsEffect(op)
        self.btnOK.setStyleSheet('background-color:blue')



