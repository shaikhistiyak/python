import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QWidget

class myapp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("some thing")

def main():
    app = QApplication(sys.argv)
    window = myapp()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()