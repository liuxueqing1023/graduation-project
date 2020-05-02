from PyQt5 import QtWidgets as qw
#from aircraft_war import run_game



class Loginfunctions():
    def __init__(self,dbPath,conn,cursor,ui,MainWindow):
        self.dbPath = dbPath
        self.conn = conn
        self.cursor = cursor
        self.ui = ui
        self.MainWindow = MainWindow

    def user_create(self):
        user_name = self.ui.nameLineEdit.text()
        user_pwd = self.ui.passwordLineEdit.text()
        sql = "insert into users (username,password) values ('%s','%s')" % (user_name,user_pwd)
        try:
            #向数据库插入数据
            self.cursor.execute(sql)
            self.conn.commit()
            #self.conn.close()
        except:
            self.conn.rollback()
    def user_delete(self):
        user_name = self.ui.nameLineEdit.text()
        user_pwd = self.ui.passwordLineEdit.text()
        sql = "delete from users where username='%s' and password='%s'" % (user_name,user_pwd)
        try:
            #向数据库插入数据
            self.cursor.execute(sql)
            self.conn.commit()
            self.conn.close()
        except:
            self.conn.rollback()
    def password_change(self):
        user_name = self.ui.nameLineEdit.text()
        user_pwd = self.ui.passwordLineEdit.text()
        sql = "update users set password='%s' where username='%s'" % (user_pwd,user_name)
        try:
            #向数据库插入数据
            self.cursor.execute(sql)
            self.conn.commit()
            #self.conn.close()
        except:
            self.conn.rollback()
    def user_deleter(self):
        user_name = self.ui.nameLineEdit.text()
        user_pwd = self.ui.passwordLineEdit.text()
        sql = "select * from users where username='%s' and password='%s'" % (user_name,user_pwd)
        if len(user_name) == 0 or len(user_pwd) == 0:
            qw.QMessageBox.information(self.MainWindow, '消息',
                                    "您的用户名或密码不能为空")
        else:
            try:
                self.cursor.execute(sql)
                result = self.cursor.fetchall()
                num = len(result)
                #print(num)
                if  num == 1:
                    qw.QMessageBox.information(self.MainWindow, '消息',
                                    "用户注销成功")
                    self.user_delete()
                else:
                    qw.QMessageBox.information(self.MainWindow, '消息',
                                "用户名或密码错误")
            except:
                self.conn.rollback()
    def password_changer(self):
        user_name = self.ui.nameLineEdit.text()
        user_pwd = self.ui.passwordLineEdit.text()
        sql = "select * from users where username='%s'" % (user_name)
        if len(user_name) == 0 or len(user_pwd) == 0:
            qw.QMessageBox.information(self.MainWindow, '消息',
                                    "您的用户名或密码不能为空")
        else:
            try:
                self.cursor.execute(sql)
                result = self.cursor.fetchall()
                num = len(result)
                #print(num)
                if  num == 1:
                    qw.QMessageBox.information(self.MainWindow, '消息',
                                    "密码修改成功")
                    self.password_change()
                else:
                    qw.QMessageBox.information(self.MainWindow, '消息',
                                "您要密码修改的用户不存在")
            except:
                self.conn.rollback()
    def user_register(self):
        user_name = self.ui.nameLineEdit.text()
        user_pwd = self.ui.passwordLineEdit.text()
        user_repwd = self.ui.confirmLineEdit.text()
        sql = "select * from users where username='%s'" % (user_name)
        if len(user_name) == 0 or len(user_pwd) == 0 or len(user_repwd) == 0:
            qw.QMessageBox.information(self.MainWindow, '消息',
                                    "您的用户名或密码不能为空")
        elif user_pwd != user_repwd:
            qw.QMessageBox.information(self.MainWindow, '消息',
                                       "您的两次密码输入不一致")
        else:
            try:
                self.cursor.execute(sql)
                result = self.cursor.fetchall()
                num = len(result)
                #print(num)
                if  num != 1:
                    qw.QMessageBox.information(self.MainWindow, '消息',
                                    "注册成功")
                    self.user_create()
                else:
                    qw.QMessageBox.information(self.MainWindow, '消息',
                                "用户已存在")
            except:
                self.conn.rollback()
    def user_login(self):
        user_name = self.ui.nameLineEdit.text()
        user_pwd = self.ui.passwordLineEdit.text()
        sql = "select * from users where username='%s' and password='%s'" % (user_name,user_pwd)
        if len(user_name) == 0 or len(user_pwd) == 0:
            qw.QMessageBox.information(self.MainWindow, '消息',
                                    "您的用户名或密码不能为空")
        else:
            try:
                self.cursor.execute(sql)
                result = self.cursor.fetchall()
                num = len(result)
                #print(num)
                if  num == 1:
                    qw.QMessageBox.information(self.MainWindow, '消息',
                                    "登录成功")
                    self.MainWindow.close()
                else:
                    qw.QMessageBox.information(self.MainWindow, '消息',
                                "用户名或密码错误")
            except:
                self.conn.rollback()
