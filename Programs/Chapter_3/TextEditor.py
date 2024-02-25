from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit

class TextEditorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setGeometry(100, 100, 400, 300)
        self.setWindowTitle('QTextEdit Example')
        
    def initUI(self):
        # Create a layout
        layout = QVBoxLayout()

        # Create a QTextEdit
        self.textEdit = QTextEdit()
        self.textEdit.setHtml('<h1>PyQt6</h1><p>This is a <b>rich text</b> editor.</p>')

        # Add TextEdit
        layout.addWidget(self.textEdit)
        button = QPushButton('Display Value')
        button.clicked.connect(self.displayValue)
        layout.addWidget(button)

        self.setLayout(layout)
    
    def displayValue(self):
        print('Plain text')
        print(self.textEdit.toPlainText())
        print('Rich text')
        print(self.textEdit.toHtml())

if __name__ == '__main__':
    app = QApplication([])
    w = TextEditorApp()
    w.show()
    app.exec()

