import sys
import sqlite3
import Personal as uw
import Login as login
import Register as res
from PyQt5 import QtWidgets as qw
from functions import Loginfunctions


class Login(qw.QMainWindow):
    def __init__(self):
        super(Login, self).__init__()
        self.dbPath = "/home/wangziwei/PycharmProjects/QtDesigner/graduate/users.db"
        self.conn = sqlite3.connect(self.dbPath)
        self.cursor = self.conn.cursor()
        self.ui = login.UiMainWindow()
        self.loginfunctions = Loginfunctions(self.dbPath, self.conn, self.cursor, self.ui, self)
        self.setWindowTitle('登录')
        # 调用Ui_setup方法动态创建控件
        self.ui.Ui_setup(self)
        self.ui.btnOK.clicked.connect(self.loginfunctions.user_login)
        self.ui.label1.linkActivated.connect(self.btnRegister_function)
        self.ui.label2.linkActivated.connect(self.btnPer_function)
        # 显示窗口

    def btnRegister_function(self):
        self.close()
        self.s = Register()
        self.s.show()

    def btnPer_function(self):
        self.close()
        self.s = Personal()
        self.s.show()


class Personal(qw.QMainWindow):
    def __init__(self):
        super(Personal, self).__init__()
        self.dbPath = "/home/wangziwei/PycharmProjects/QtDesigner/graduate/users.db"
        self.conn = sqlite3.connect(self.dbPath)
        self.cursor = self.conn.cursor()
        self.ui = uw.UiMainWindow()

        self.loginfunctions = Loginfunctions(self.dbPath, self.conn, self.cursor, self.ui, self)
        self.ui.Ui_setup(self)
        self.ui.label1.linkActivated.connect(self.loginfunctions.user_deleter)
        self.ui.label2.linkActivated.connect(self.loginfunctions.password_changer)
        self.ui.btnReturn.clicked.connect(self.btnReturn_function)
        # 显示窗口

    def btnReturn_function(self):
        self.close()
        self.f = Login()
        self.f.show()


class Register(qw.QMainWindow):
    def __init__(self):
        super(Register, self).__init__()
        self.dbPath = "/home/wangziwei/PycharmProjects/QtDesigner/graduate/users.db"
        self.conn = sqlite3.connect(self.dbPath)
        self.cursor = self.conn.cursor()
        self.ui = res.RegisterWindow()

        self.loginfunctions = Loginfunctions(self.dbPath, self.conn, self.cursor, self.ui, self)
        self.ui.Ui_setup(self)
        self.ui.btnSign.clicked.connect(self.loginfunctions.user_register)
        self.ui.btnReturn.clicked.connect(self.btnReturn_function)
        # 显示窗口

    def btnReturn_function(self):
        self.close()
        self.f = Login()
        self.f.show()


def main():
    app = qw.QApplication(sys.argv)
    w = Login()
    w.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()