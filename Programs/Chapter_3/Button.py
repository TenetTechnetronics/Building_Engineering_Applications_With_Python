import os
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
from PyQt6.QtGui import QIcon

# local machine repository path
path = os.environ.get('SampleProgram')

class ButtonApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setGeometry(100, 100, 400, 300)
        
    def initUI(self):
        layout = QVBoxLayout()
        
		
        # Create a button
        self.button = QPushButton('Save', self)
        
		# Create icon with image page
        icon = QIcon(path + 'assets/images/save_icon.png')
		# Set icon to button
        self.button.setIcon(icon)
        
        layout.addWidget(self.button)
        layout.setContentsMargins(100, 100, 100, 100)
        # Create Event handler
        self.button.clicked.connect(self.onButtonClick)
        self.setLayout(layout)

    # Event Handler function
    def onButtonClick(self):
        print('Save Button clicked!')

if __name__ == '__main__':
    app = QApplication([])
    w = ButtonApp()
    w.show()
    app.exec()
