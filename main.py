import sys
from PyQt5.QtWidgets import QApplication,QMainWindow

class Myapp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("some")
        self.setGeometry(0,0,500,500)
        self.setFixedHeight(450)
        self.setMaximumHeight(400)


def main():
    a = QApplication(sys.argv)
    app = Myapp()
    app.show()
    sys.exit(a.exec_())

if __name__ == "__main__":
    main()