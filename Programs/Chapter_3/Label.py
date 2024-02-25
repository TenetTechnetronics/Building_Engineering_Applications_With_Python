import os
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel 
from PyQt6.QtGui import QFont, QPixmap
from PyQt6.QtCore import Qt

# local machine repository path
path = os.environ.get('SampleProgram')

class LabelApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setGeometry(100, 100, 400, 300)
        
    def initUI(self):
        # Create a layout
        layout = QVBoxLayout()
        
        label = QLabel('Hello, PyQt6!')
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(25)
        label.setFont(font)
        
        # Set the color, You can use stylesheet to set font also 
        label.setStyleSheet("color: red")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label)

        imageLabel = QLabel()
        # Load the image
        pixmap = QPixmap(path + 'assets/images/save_icon.png')
        # Set the image in the QLabel widget
        imageLabel.setPixmap(pixmap)
        layout.addWidget(imageLabel)

        layout.setContentsMargins(100, 100, 100, 100)
        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication([])
    w = LabelApp()
    w.show()
    app.exec()
