from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit

class TextboxApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setGeometry(100, 100, 400, 300)
        self.setWindowTitle('QLineEdit Example')
        
    def initUI(self):
        # Create a layout
        layout = QVBoxLayout()

        # Create a QLineEdit
        self.lineEdit = QLineEdit()
        self.lineEdit.setPlaceholderText('Enter your text here')
        # Text changed
        self.lineEdit.textChanged.connect(self.updateValue)
        # Return Pressed
        self.lineEdit.returnPressed.connect(self.returnText)
        # set maximum length user can enter in textbox
        self.lineEdit.setMaxLength(10)
        # In case you need to disable textbox
        #self.lineEdit.setReadOnly(True)

        # Add LineEdit
        layout.addWidget(self.lineEdit)

        self.label = QLabel('Textbox Value')
        
        # Add Label
        layout.addWidget(self.label)

        self.setLayout(layout)
    
    def updateValue(self):
        self.label.setText(self.lineEdit.text())

    def returnText(self):
        print('Texbox value when return pressed - ' + self.lineEdit.text())

if __name__ == '__main__':
    app = QApplication([])
    w = TextboxApp()
    w.show()
    app.exec()

