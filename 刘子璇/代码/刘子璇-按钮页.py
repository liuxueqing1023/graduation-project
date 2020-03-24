from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import sys,math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class QPushButtonDemo(QDialog):
    def __init__(self):
        super(QPushButtonDemo,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QPushButton Demo')

        layout = QVBoxLayout()

        self.button1 = QPushButton('第一个按钮')
        self.button1.setText('First Button1')
        self.button1.setCheckable(True)
        # 使按钮处于选中状态，再调用一次，取消选中状态
        self.button1.toggle()
        # lambda
        self.button1.clicked.connect(lambda :self.whichButton(self.button1))
        self.button1.clicked.connect(self.buttonState)
        layout.addWidget(self.button1)

        # 在文本前面显示图像
        self.button2 = QPushButton('图像按钮')
        self.button2.setIcon(QIcon(QPixmap('/home/liuzixuan/实训/PyQt5视频教程/images/style01.jpg')))
        self.button2.clicked.connect(lambda :self.whichButton(self.button2))
        layout.addWidget(self.button2)

        # 不可用的按钮
        self.button3 = QPushButton('不可用的按钮')
        self.button3.setEnabled(False)
        layout.addWidget(self.button3)

        # 默认的按钮（按回车键,自动调用默认的按钮）,默认的按钮一个窗口只能有一个
        self.button4 = QPushButton('&MyButton')
        self.button4.setDefault(True)
        self.button4.clicked.connect(lambda :self.whichButton(self.button4))
        layout.addWidget(self.button4)

        self.setLayout(layout)
        self.resize(400,300)

    def whichButton(self,btn):
        print('被单击的按钮是<' + btn.text() + '>')

    def buttonState(self):
        if self.button1.isChecked():
            print('按钮１已经被选中')
        else:
            print('按钮１未被选中')








class ButtonPage(QMainWindow):
    def __init__(self):
        super(ButtonPage,self).__init__()
        self.setWindowTitle('按钮页')
        self.resize(400,800)
        self.move(800,100)

        self.setStyleSheet("QMainWindow{border-image:url(/home/liuzixuan/实训/PyQt5视频教程/images/background4.jpg)}")

        label = QLabel(self)
        label.setAlignment(Qt.AlignCenter)
        label.setFixedSize(70,70)
        label.setGeometry(170,120,70,70)
        label.setStyleSheet("QLabel{border:1px solid;"
                            "min-width:60px;"
                            "min-height:60px;"
                            "max-width:60px;"
                            "max-height:60px;"
                            "border-radius:30px;"
                            "border-color:rgb(245,245,245);"
                            "border-image:url(/home/liuzixuan/实训/PyQt5视频教程/images/logo2.jpg);}")
        #label.setPixmap(QPixmap('/home/liuzixuan/实训/PyQt5视频教程/images/logo2.jpg'))
        # 图片自适应label大小
        #label.setScaledContents(True)
        #layout.addWidget(label)
        #self.setLayout(layout)


        btn1 = QPushButton(self)
        btn1.setText("首       页")
        btn1.move(60, 220)
        btn1.setFixedSize(280,40)
        btn1.setFont(QFont("华文新魏", 14))
        btn1.setStyleSheet("QPushButton{background:rgb(230,230,250);"
                           "font-style:华文新魏;"
                           "font-size:20px;"
                           "color:rgb(192,192,192);"
                           "border:1px solid;"
                           "border-radius:10px;"
                           "border-color:rgb(245,245,245);"
                           "-moz-border-radius:10px;}")
        btn1.clicked.connect(self.shouye)

        btn2 = QPushButton(self)
        btn2.setText("创       意")
        btn2.move(60, 290)
        btn2.setFixedSize(280,40)
        btn2.setFont(QFont("华文新魏", 14))
        btn2.setStyleSheet("QPushButton{background:rgb(230,230,250);"
                           "font-style:华文新魏;"
                           "font-size:20px;"
                           "color:rgb(192,192,192);"
                           "border:1px solid;"
                           "border-radius:10px;"
                           "border-color:rgb(245,245,245);"
                           "-moz-border-radius:10px;}")
        btn2.clicked.connect(self.chuangyi)

        btn3 = QPushButton(self)
        btn3.setText("我       的")
        btn3.move(60, 360)
        btn3.setFixedSize(280,40)
        btn3.setFont(QFont("华文新魏", 14))
        btn3.setStyleSheet("QPushButton{background:rgb(230,230,250);"
                           "font-style:华文新魏;"
                           "font-size:20px;"
                           "color:rgb(192,192,192);"
                           "border:1px solid;"
                           "border-radius:10px;"
                           "border-color:rgb(245,245,245);"
                           "-moz-border-radius:10px;}")
        btn3.clicked.connect(self.wode)

    def shouye(self):
        self.hide()
        self.sy = QPushButtonDemo()
        self.sy.show()

        # 退出应用程序
        #app = QApplication.instance()
        #app.quit()



    def chuangyi(self):
        pass

    def wode(self):
        pass



if __name__=='__main__':
    app = QApplication(sys.argv)

    main = ButtonPage()
    main.show()

    sys.exit(app.exec_())