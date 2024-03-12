from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt6.QtCore import Qt, pyqtSignal, QObject, pyqtSignal

class CustomSignal(QObject):
    # Custom Signal
    signal = pyqtSignal(str)

class ChildWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.customSignal = CustomSignal()
        
        layout = QVBoxLayout()

        # Create a button
        button = QPushButton("Click Me", self)
        button.clicked.connect(self.onButtonClick)
        self.count = 0

        layout.addWidget(button)
        self.setLayout(layout)

    def onButtonClick(self):
        self.count = self.count + 1
        # Emit the custom signal with a value
        self.customSignal.signal.emit(str(self.count))


class CustomSignalSlotApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setGeometry(100, 100, 400, 300)
        
    def initUI(self):
        self.childWidget = ChildWidget()

        layout = QVBoxLayout()
        layout.addWidget(self.childWidget)
        self.parentLabel = QLabel("Click Count 0")
        layout.addWidget(self.parentLabel, 0, Qt.AlignmentFlag.AlignCenter)
        
        self.setLayout(layout)
        # Connect slot to custom signal
        self.childWidget.customSignal.signal.connect(self.onSignalRecieved)
    
    def onSignalRecieved(self, value):
        self.parentLabel.setText("Click Count " + value)
        if(int(value) == 5):
            # Disconnect slot from custom signal
            self.childWidget.customSignal.signal.disconnect(self.onSignalRecieved)

if __name__ == '__main__':
    app = QApplication([])
    w = CustomSignalSlotApp()
    w.show()
    app.exec()
