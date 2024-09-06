import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QLabel
from PyQt5.QtGui import QFont,QPixmap
from PyQt5.QtCore import Qt
class app(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("hello every one to my appication")
        self.setGeometry(300,150,500,500)
        # self.setGeometry(self.height()-1366,self.width()-768,500,500)
        greeting = QLabel("hello every one to my app",self)
        greeting.setGeometry(0,0,self.width(),50)
        greeting.setFont(QFont("arial",20,0,True))
        greeting.setStyleSheet("color:white;"
                                "background-color:black;"
                                "font-style:italic;"
                                "text-decoration:underline;")
        greeting.setAlignment(Qt.AlignTop)
        greeting.setAlignment(Qt.AlignBottom)
        greeting.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
        p = QLabel(self)
        p.setGeometry(0,50,self.width(),self.height()-50)
        # pic = QPixmap("telegram-app-logo.png") 
        pic = QPixmap("tutorial_env\\telegram-app-logo.png") 
        p.setPixmap(pic)
        p.setScaledContents(True)
        
        


def main():
    system = QApplication(sys.argv)
    window = app()
    window.show()
    sys.exit(system.exec_())

if __name__ == "__main__":
    main()