import sys
from PyQt5.QtWidgets import QMainWindow,QApplication,QVBoxLayout, QHBoxLayout, QLabel, QWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QPalette,QBrush


class FirstMainWin(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.initUI()

    def initUI(self):

        #设置主窗口标题
        self.setWindowTitle('首页')

        #设置主窗口尺寸
        self.resize(400, 700)


        # 设置背景
        palette = QPalette()
        #palette1.setBrush(self.backgroundRole(), QBrush(QPixmap('/home/wangziwei/Pictures/1.jpg')))  # 设置背景图片
        #self.setPalette(palette1)
        pix = QPixmap('/home/wangziwei/Pictures/1.jpg').scaled(self.width(), self.height())
        palette.setBrush(QPalette.Background, QBrush(pix))
        self.setPalette(palette)

        label1 = QLabel(self)
        label2 = QLabel(self)
        label3 = QLabel(self)
        label4 = QLabel(self)
        label5 = QLabel(self)
        label6 = QLabel(self)

        label1.setText('<font color = white>目前市场上推出的美颜相机不计其数，'
                       '功能大多是大同小异，包美颜、滤镜、贴纸等功能，但是很明显的'
                       '一个缺陷是，人们在使用时，只能选择软件自带而模板，我们这是'
                       '一款能自定义生成某种特定特征的滤镜的软件。</font>''<a href = "#">返回</a>')
        label1.setWordWrap(True)

        label2.setPixmap(QPixmap('/home/wangziwei/Pictures/a.jpg').scaled(200, 150))
        label3.setPixmap(QPixmap('/home/wangziwei/Pictures/b.jpg').scaled(200, 150))
        label4.setPixmap(QPixmap('/home/wangziwei/Pictures/c.jpg').scaled(200, 150))
        label5.setPixmap(QPixmap('/home/wangziwei/Pictures/d.jpg').scaled(200, 150))




        wbox = QVBoxLayout()
        vbox = QHBoxLayout()
        hbox1 = QHBoxLayout()
        hbox2 = QHBoxLayout()

        vbox.addWidget(label1)
        hbox1.addWidget(label2)
        hbox1.addWidget(label3)
        hbox2.addWidget(label4)
        hbox2.addWidget(label5)

        vwg = QWidget()
        hwg1 = QWidget()
        hwg2 = QWidget()

        vwg.setLayout(vbox)
        hwg1.setLayout(hbox1)
        hwg2.setLayout(hbox2)

        wbox.addWidget(vwg)
        wbox.addWidget(hwg1)
        wbox.addWidget(hwg2)
        self.setLayout(wbox)



if __name__ == '__main__':
    app = QApplication(sys.argv)

    main = FirstMainWin()
    main.show()

    sys.exit(app.exec_())