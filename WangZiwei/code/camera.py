import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import cv2

import time


class Picture(QWidget):
    def __init__(self):
        super(Picture, self).__init__()
        # 设置主窗口标题
        self.setWindowTitle('首页')

        # 设置主窗口尺寸
        self.resize(400, 700)

        self.label1 = QLabel(self)
        button1 = QPushButton(self)
        button1.setText('选择图片')
        button1.clicked.connect(self.openimage)


        self.button2 = QPushButton()
        self.button2.setCheckable(True)
        self.button2.toggle()  # 处于选中状态,再调用一次就处于未选中状态
        self.button2.setIcon(QIcon(QPixmap('../../camera.jpg')))

        self.button3 = QPushButton()
        self.button3.setIcon(QIcon(QPixmap('../../camera1.jpg')))
        self.button3.clicked.connect(self.closeEvent)


        label2 = QLabel(self)

        self.label1.setText('内容图片')
        self.label1.setFixedSize(350, 350)
        self.label1.setAlignment(Qt.AlignCenter)
        self.label1.setStyleSheet("QLabel{background:white;}"
                                  "QLabel{color:rgb(300,300,300,120);}"
                                  "font-size:10px;font-weight:bold;font-family:宋体;}")


        label2.setText('风格图片')
        label2.setFixedSize(200, 200)
        label2.setAlignment(Qt.AlignCenter)
        label2.setStyleSheet("QLabel{background:white;}"
                             "QLabel{color:rgb(300,300,300,120);}"
                             "font-size:10px;font-weight:bold;font-family:宋体;}")



        vBox = QVBoxLayout()
        hBox = QHBoxLayout()
        hwg = QWidget()

        hBox.addStretch(1)
        hBox.addWidget(button1)
        hBox.addStretch(1)
        hBox.addWidget(self.button2)
        hBox.addStretch(1)
        hBox.addWidget(self.button3)
        hBox.addStretch(1)
        hwg.setLayout(hBox)

        # vBox.addStretch(0)
        vBox.addWidget(self.label1)
        # vBox.addStretch(1)
        vBox.addWidget(hwg)
        # vBox.addStretch(0)
        vBox.addWidget(label2)
        self.setLayout(vBox)

        self.timer_camera = QtCore.QTimer()  # 定时器
        #self.setupUi(MainWindow)
        #self.retranslateUi(MainWindow)
        self.cap = cv2.VideoCapture()  # 准备获取图像
        self.CAM_NUM = 0
        self.n = 1
        self.slot_init()  # 设置槽函数



    #def buttonState(self):
    #    if self.button2.isChecked():
    #        print(1)
    #        self.takePhoto()
    #        self.button2.setIcon(QIcon(QPixmap('../../camera2.jpg')))
    #        #self.button2.clicked.connect(self.button_open_camera_click)
    #    else:
    #        print(2)
    #        self.button_open_camera_click()
    #        self.button2.setIcon(QIcon(QPixmap('../../camera.jpg')))
    #        #self.button2.clicked.connect(self.takePhoto)

    def buttonState(self, n):
        if self.n == 1:
            self.button_open_camera_click()
            self.button2.setIcon((QIcon(QPixmap('../../camera'))))
            self.n = 2
        else:
            self.takePhoto()
            self.button2.setIcon(QIcon(QPixmap('../../camera2.jpg')))
            self.n = 1



    def openimage(self):
        # sender = self.sender()
        imgName, imgType = QFileDialog.getOpenFileName(self, "打开图片", "", "*.jpg;;*.png;;All Files(*)")
        # if sender.text() == '选择图片 ':
        jpg = QtGui.QPixmap(imgName).scaled(self.label1.width(), self.label1.height())
        self.label1.setPixmap(jpg)
        # else:
        #    jpg = QtGui.QPixmap(imgName).scaled(self.label2.width(), self.label2.height())
        #    self.label2.setPixmap(jpg)




    def slot_init(self):
        # 设置槽函数
        #self.button2.clicked.connect(self.show_camera)
        #self.button3.clicked.connect()
        self.button2.clicked.connect(self.buttonState)
        self.timer_camera.timeout.connect(self.show_camera)

    def button_open_camera_click(self):
        if self.timer_camera.isActive() == False:
            flag = self.cap.open(self.CAM_NUM)
            if flag == False:
                msg = QtWidgets.QMessageBox.warning(
                    self, u"Warning", u"请检测相机与电脑是否连接正确",
                    buttons=QtWidgets.QMessageBox.Ok,
                    defaultButton=QtWidgets.QMessageBox.Ok)
            else:
                self.timer_camera.start(30)

    def show_camera(self):
        flag, self.image = self.cap.read()

        self.image = cv2.flip(self.image, 1)  # 左右翻转
        show = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)

        showImage = QtGui.QImage(show.data, show.shape[1], show.shape[0], QtGui.QImage.Format_RGB888)
        self.label1.setPixmap(QtGui.QPixmap.fromImage(showImage))
        self.label1.setScaledContents(True)


    def takePhoto(self):
        if self.timer_camera.isActive() != False:
            now_time = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))
            print(now_time)
            cv2.imwrite('pic_' + str(now_time) + '.png', self.image)

            #cv2.putText(self.image, 'The picture have saved !',
            #            (int(self.image.shape[1] / 2 - 130), int(self.image.shape[0] / 2)),
            #            cv2.FONT_HERSHEY_SCRIPT_COMPLEX,
            #            1.0, (255, 0, 0), 1)

            self.timer_camera.stop()  # 停止计时

            show = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)  # 左右翻转

            showImage = QtGui.QImage(show.data, show.shape[1], show.shape[0], QtGui.QImage.Format_RGB888)
            self.label1.setPixmap(QtGui.QPixmap.fromImage(showImage))
            self.label1.setScaledContents(True)

    def closeEvent(self):
        if self.timer_camera.isActive() != False:
            ok = QtWidgets.QPushButton()
            cacel = QtWidgets.QPushButton()

            # 提示信息
            msg = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Warning, u"关闭", u"是否关闭！")
            msg.addButton(ok, QtWidgets.QMessageBox.ActionRole)
            msg.addButton(cacel, QtWidgets.QMessageBox.RejectRole)
            ok.setText(u'确定')
            cacel.setText(u'取消')

            if msg.exec_() != QtWidgets.QMessageBox.RejectRole:
                # 停止获取画面
                if self.cap.isOpened():
                    self.cap.release()
                if self.timer_camera.isActive():
                    self.timer_camera.stop()
                self.label1.setText('内容图片')
                self.n = 1



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Picture()
    main.show()

    sys.exit(app.exec_())







