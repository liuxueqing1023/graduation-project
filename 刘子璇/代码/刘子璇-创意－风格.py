from __future__ import print_function
from scipy.optimize import fmin_l_bfgs_b
import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import numpy as np
from PIL import Image
from keras import backend
from keras.applications.vgg16 import VGG16

import cv2
import time
import os


content_weight = 0.025
style_weight = 5.0
height = 400
width = 400

def chuli(b):
    image = Image.open(b)
    image = image.resize((400, 400))
    array = np.asarray(image, dtype='float32')
    array = np.expand_dims(array, axis=0)
    array[:, :, :, 0] -= 103.939
    array[:, :, :, 1] -= 116.779
    array[:, :, :, 2] -= 123.68
    array = array[:, :, :, ::-1]
    return array

def content_loss(content, combination):
    return backend.sum(backend.square(combination - content))


def gram_matrix(x):
    features = backend.batch_flatten(backend.permute_dimensions(x, (2, 0, 1)))
    gram = backend.dot(features, backend.transpose(features))
    return gram

def style_loss(style, combination):
    S = gram_matrix(style)
    C = gram_matrix(combination)
    channels = 3
    size = height * width
    return backend.sum(backend.square(S - C)) / (4. * (channels ** 2) * (size ** 2))

def total_variation_loss(x):
    a = backend.square(x[:, :height - 1, :width - 1, :] - x[:, 1:, :width - 1, :])
    b = backend.square(x[:, :height - 1, :width - 1, :] - x[:, :height - 1, 1:, :])
    return backend.sum(backend.pow(a + b, 1.25))



class Creative(QMainWindow):
    content_array = np.arange(480000).reshape(1, 400, 400, 3)
    style_array = np.arange(480000).reshape(1, 400, 400, 3)
    combination_image = backend.placeholder((1, height, width, 3))
    x = 0

    def __init__(self):
        super(Creative,self).__init__()
        self.setWindowTitle('创意－风格')
        self.resize(400,800)
        self.move(800,100)

        self.setStyleSheet("QMainWindow{border-image:url(/home/liuzixuan/实训/PyQt5视频教程/images/background4.jpg)}")


        self.btn1 = QPushButton(self)
        self.btn1.move(100,100)
        self.btn1.setFixedSize(160,200)
        self.btn1.setStyleSheet("QPushButton{border-image:url(/home/liuzixuan/实训/02-用Python快速实现图片的风格迁移/img/img01.jpg);}")

        self.btn2 = QPushButton(self)
        self.btn2.setText('内容')
        self.btn2.move(180,320)
        self.btn2.setFixedSize(30,30)
        self.btn2.clicked.connect(self.open_content_image)

        self.btn3 = QPushButton(self)
        self.btn3.move(130, 360)
        self.btn3.setFixedSize(100,120)
        self.btn3.setStyleSheet("QPushButton{border-image:url(/home/liuzixuan/实训/02-用Python快速实现图片的风格迁移/style_img/style05.jpg);}")
        style_imgName = '/home/liuzixuan/实训/02-用Python快速实现图片的风格迁移/style_img/style05.jpg'
        a = chuli(style_imgName)
        self.style_array = a
        self.style_array = backend.variable(self.style_array)
        self.btn3.clicked.connect(self.vgg)

        self.btn4 = QPushButton(self)
        self.btn4.setText("风格")
        self.btn4.move(140, 320)
        self.btn4.setFixedSize(30,30)
        self.btn4.clicked.connect(self.open_style_image)
        self.btn4.clicked.connect(self.vgg)



    def vgg(self):
        input_tensor = backend.concatenate([self.content_array,
                                            self.style_array,
                                            self.combination_image], axis=0)
        model = VGG16(input_tensor=input_tensor, weights='imagenet',
                      include_top=False)
        layers = dict([(layer.name, layer.output) for layer in model.layers])

        total_variation_weight = 1.0
        loss = backend.variable(0.)

        layer_features = layers['block2_conv2']
        content_image_features = layer_features[0, :, :, :]
        combination_features = layer_features[2, :, :, :]

        loss = loss + content_weight * content_loss(content_image_features,
                                              combination_features)

        feature_layers = ['block1_conv2', 'block2_conv2',
                          'block3_conv3', 'block4_conv3',
                          'block5_conv3']

        for layer_name in feature_layers:
            layer_features = layers[layer_name]
            style_features = layer_features[1, :, :, :]
            combination_features = layer_features[2, :, :, :]
            sl = style_loss(style_features, combination_features)
            loss = loss + (style_weight / len(feature_layers)) * sl

        loss =loss + total_variation_weight * total_variation_loss(self.combination_image)

        grads = backend.gradients(loss, self.combination_image)

        outputs = [loss]
        outputs = outputs + grads
        f_outputs = backend.function([self.combination_image], outputs)

        def eval_loss_and_grads(x):
            x = x.reshape((1, height, width, 3))
            outs = f_outputs([x])
            loss_value = outs[0]
            grad_values = outs[1].flatten().astype('float64')
            return loss_value, grad_values

        class Evaluator(object):
            def __init__(self):
                self.loss_value = None
                self.grads_values = None

            def loss(self, x):
                assert self.loss_value is None
                loss_value, grad_values = eval_loss_and_grads(x)
                self.loss_value = loss_value
                self.grad_values = grad_values
                return self.loss_value

            def grads(self, x):
                assert self.loss_value is not None
                grad_values = np.copy(self.grad_values)
                self.loss_value = None
                self.grad_values = None
                return grad_values

        evaluator = Evaluator()
        x = np.random.uniform(0, 255, (1, height, width, 3)) - 128.
        iterations = 5
        for i in range(iterations):
            x, min_val, info = fmin_l_bfgs_b(evaluator.loss, x.flatten(),
                                             fprime=evaluator.grads, maxfun=20)
        x = x.reshape((height, width, 3))
        x = x[:, :, ::-1]
        x[:, :, 0] += 103.939
        x[:, :, 1] += 116.779
        x[:, :, 2] += 123.68
        x = np.clip(x, 0, 255).astype('uint8')

        image = Image.fromarray(x)
        image.save('./out.jpg')
        self.btn1.setStyleSheet("QPushButton{border-image:url(./out.jpg);}")



    def open_content_image(self):
        imgName, imgType = QFileDialog.getOpenFileName(self, "打开图片", "", "*.jpg;;*.png;;All Files(*)")
        a = chuli(imgName)
        self.content_array = a
        self.content_array = backend.variable(self.content_array)


    def open_style_image(self):
        imgName, imgType = QFileDialog.getOpenFileName(self, "打开图片", "", "*.jpg;;*.png;;All Files(*)")
        a = chuli(imgName)
        self.style_array = a
        self.style_array = backend.variable(self.style_array)







if __name__=='__main__':
    app = QApplication(sys.argv)

    main = Creative()
    main.show()

    sys.exit(app.exec_())
