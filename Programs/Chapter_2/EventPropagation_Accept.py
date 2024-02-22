import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel

class ChildWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setLayout(QVBoxLayout())
        self.label = QLabel('Click on Child widget.')
        self.layout().addWidget(self.label)

    def mousePressEvent(self, event):
        print('Sub Child Event triggered.')
        # Accept the event
        event.accept()

class ParentWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setLayout(QVBoxLayout())
        self.subChild = ChildWidget()
        self.layout().addWidget(self.subChild)
        self.setGeometry(400,200,400,400)

    def mousePressEvent(self, event):
        print('Event Reached Parent')
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = ParentWidget()
    w.show()
    

    app.exec()