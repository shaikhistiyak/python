import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QWidget,QLabel,QVBoxLayout,QHBoxLayout,QGridLayout

class myapp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("some")
        self.setGeometry(250,150,500,500)
        self.setUi()
    def setUi(self):
        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)

        lable1 = QLabel("lable1",self)
        lable2 = QLabel("lable2",self)
        lable3 = QLabel("lable3",self)
        lable1.setStyleSheet("background-color: red;")
        lable2.setStyleSheet("background-color: brown;")
        lable3.setStyleSheet("background-color: lightgreen;")
        #vbox layout
        vbox = QVBoxLayout()
        vbox.addWidget(lable1)
        vbox.addWidget(lable2)
        vbox.addWidget(lable3)
        # centralWidget.setLayout(vbox)
        #hbox layout
        hbox = QHBoxLayout()
        hbox.addWidget(lable1)
        hbox.addWidget(lable2)
        hbox.addWidget(lable3)
        # centralWidget.setLayout(hbox)
        gbox =QGridLayout()
        gbox.addWidget(lable1,0,0)
        gbox.addWidget(lable2,0,2)
        gbox.addWidget(lable3,2,0)
        centralWidget.setLayout(gbox)

def main():
    app = QApplication(sys.argv)
    window = myapp()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()