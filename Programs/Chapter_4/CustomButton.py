from PyQt6.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout, QLabel
from PyQt6.QtCore import pyqtSignal, Qt

class CustomButton(QPushButton):
    # Define Custom signal
    sendCustomMessage = pyqtSignal(str)

    def __init__(self, title, parent=None):
        super().__init__(title, parent)
        self.title = title
        # Emit custom signal on click
        self.clicked.connect(self.emitCustomSignal)

    def emitCustomSignal(self):
        # Emit the custom signal with a message
        self.sendCustomMessage.emit(self.title + " clicked!")

class AppWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Custom Widget")
        self.setGeometry(200, 200, 400, 300)
        mainLayout = QVBoxLayout()
        
        layout1 = QVBoxLayout()
        button1 = CustomButton("Layout 1 Button")
        button1.sendCustomMessage.connect(self.onButtonClick)
        layout1.addWidget(button1)
        mainLayout.addLayout(layout1)

        layout2 = QVBoxLayout()
        button2 = CustomButton("Layout 2 Button")
        button2.sendCustomMessage.connect(self.onButtonClick)        
        layout2.addWidget(button2)
        mainLayout.addLayout(layout2)
        
        layout3 = QVBoxLayout()
        self.label = QLabel("Label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout3.addWidget(self.label)
        mainLayout.addLayout(layout3)
        self.setLayout(mainLayout)
    
    def onButtonClick(self, message):
        self.label.setText(message)

if __name__ == "__main__":
    app = QApplication([])
    window = AppWindow()
    window.show()
    app.exec()
