from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setMinimumWidth(400)
        self.setMinimumHeight(400)
        
    def initUI(self):
        self.count = 0
        layout = QVBoxLayout()
        # Create a button
        self.button = QPushButton('Click', self)
        
        # Create Event handler
        self.button.clicked.connect(self.onButtonClick)

        layout.addWidget(self.button)
        layout.setContentsMargins(100,100,100,100)
        self.setLayout(layout)

    # Event Handler function
    def onButtonClick(self):
        self.count = self.count + 1
        self.button.setText('Clicked '+ str(self.count))

if __name__ == '__main__':
    # Initialize the PyQt application 
    app = QApplication([])
    # Create a window
    w = MyApp()
    # Display the window
    w.show()
    # Start the event loop
    app.exec()
