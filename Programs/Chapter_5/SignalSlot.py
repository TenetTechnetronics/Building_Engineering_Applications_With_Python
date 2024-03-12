from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton

class SignalSlotApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setGeometry(100, 100, 400, 300)
        
    def initUI(self):
        # Create a layout
        layout = QVBoxLayout()
        
        # Create a button
        self.button = QPushButton('Click', self)

        layout.addWidget(self.button)
        
        # Add a Slot to the Signal 
        self.button.clicked.connect(self.onButtonClick)
        self.setLayout(layout)

    # Slot function
    def onButtonClick(self):
        print('Button clicked!')

if __name__ == '__main__':
    app = QApplication([])
    w = SignalSlotApp()
    w.show()
    app.exec()
