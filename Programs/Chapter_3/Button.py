from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton

class ButtonApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setGeometry(100, 100, 400, 300)
        
    def initUI(self):
        
        # Create a button
        self.button = QPushButton('Click Me', self)
        
        # Create a Event handler
        self.button.clicked.connect(self.onButtonClick)

    # Event Handler function
    def onButtonClick(self):
        print('Button clicked!')

if __name__ == '__main__':
    app = QApplication([])
    w = ButtonApp()
    w.show()
    app.exec()
