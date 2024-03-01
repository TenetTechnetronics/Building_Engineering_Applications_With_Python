from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QComboBox

class ComboBoxApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setGeometry(100, 100, 400, 300)
        self.setWindowTitle('QComboBox Example')
        
    def initUI(self):
        # Create a layout
        layout = QVBoxLayout()
        
        # Create a QComboBox
        self.comboBox = QComboBox()
        # Add multiple items to the QComboBox
        self.comboBox.addItems(['Option 1', 'Option 2', 'Option 3', 'Option 4'])
        # Add single item
        self.comboBox.addItem('Option 5', userData="This is Option 5")
        self.comboBox.setEditable(True)

        # Add combobox
        layout.addWidget(self.comboBox)

        # Trigger on Index changed
        self.comboBox.currentIndexChanged.connect(self.onSelectedIndexChanged)
        # Trigger on Text changed
        self.comboBox.currentTextChanged.connect(self.onTextChanged)

        # Add button to remove item from list
        button = QPushButton('Remove Item')

        # Remove item on Click
        button.clicked.connect(self.removeItem)
        layout.addWidget(button)

        self.setLayout(layout)
    
    def onSelectedIndexChanged(self, index):
        print('item ', index, self.comboBox.currentIndex())
        print('Selected Text', self.comboBox.currentText())

    def onTextChanged(self, itemText):
        print('onTextChanged  ', itemText)

    def removeItem(self):
        print('Before Remove Item count ', self.comboBox.count())
        self.comboBox.removeItem(2)
        print('After Remove Item count ', self.comboBox.count())

if __name__ == '__main__':
    app = QApplication([])
    w = ComboBoxApp()
    w.show()
    app.exec()

