from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QLabel, QTextEdit
import sys

from PyQt5.QtGui import QPixmap


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Open File"
        self.top = 200
        self.left = 500
        self.width = 400
        self.height = 300

        self.InitWindow()

    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        vbox = QVBoxLayout()

        self.btn1 = QPushButton("Open Image")
        self.btn1.clicked.connect(self.getImage)

        vbox.addWidget(self.btn1)

        self.label = QLabel("Hello")
        vbox.addWidget(self.label)

        self.setLayout(vbox)

        self.show()

    def addImage(self):
        image_path = 'in_data\images\validation\0a3a42c94d470fe1952d600af7a3629fccee767925a6512d197d50be3d2deeea.png'
        qpixmap = QPixmap(image_path)

    def getImage(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '',
                                            "Image files (*.png)")
        imagePath = fname[0]
        pixmap = QPixmap(imagePath)
        self.label.setPixmap(QPixmap(pixmap))
        self.resize(pixmap.width(), pixmap.height())
        image_path = 'in_data\images\validation\0a3a42c94d470fe1952d600af7a3629fccee767925a6512d197d50be3d2deeea.png'
        qpixmap = QPixmap(image_path)
        self.resize(qpixmap.width(), qpixmap.height())

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())