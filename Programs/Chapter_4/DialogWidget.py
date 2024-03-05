from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QMessageBox, QPushButton, QDialog, QLabel, QLineEdit, QComboBox

# Custom Dialog class
class CustomDialog(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.setWindowTitle('Custom Dialog')
        self.setMinimumWidth(300)
        self.setMinimumHeight(300)

        # Layout and widgets
        layout = QVBoxLayout()
        label1 = QLabel("Enter your name:", self)
        nameEdit = QLineEdit(self)
        label2 = QLabel("Enter your DOB:", self)
        dobEdit = QLineEdit(self)

        label3 = QLabel("Select Gender:", self)
        genderCombo = QComboBox(self)
        genderCombo.addItems(['Male', 'Female'])

        button = QPushButton("OK", self)
        button.setMaximumWidth(75)

        layout.addWidget(label1)
        layout.addWidget(nameEdit)
        layout.addWidget(label2)
        layout.addWidget(dobEdit)
        layout.addWidget(label3)
        layout.addWidget(genderCombo)
        layout.addWidget(button)

        self.setLayout(layout)

        button.clicked.connect(self.okClicked)

    def okClicked(self):
        # Write logic to process input here

        # Closes the dialog and Accept
        self.accept()

class DialogWidgetApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setGeometry(100, 100, 500, 600)
        self.setWindowTitle('Dialogs Example')
        
    def initUI(self):
        # Create a layout
        hLayout = QHBoxLayout()
        button1 = QPushButton("Information Dailog")
        button2 = QPushButton("User Input Dialog")
        button1.clicked.connect(self.infoDialog)
        button2.clicked.connect(self.userDialog)
        hLayout.addWidget(button1)
        hLayout.addWidget(button2)

        self.setLayout(hLayout)

    def infoDialog(self):
        # Create QMessageBox to show information 
        dlg = QMessageBox(self)
        # Set Title for Dialog
        dlg.setWindowTitle("Information:")
        # Set Information to display
        dlg.setText("This is a information Dialog!")
        # Set Icon
        dlg.setIcon(QMessageBox.Icon.Information)
        dlg.exec()
        
    def userDialog(self):
        # intialize custom dialog
        customDialog = CustomDialog(self)
        # Show custom dialog to get user information
        customDialog.show()

if __name__ == '__main__':
    app = QApplication([])
    w = DialogWidgetApp()
    w.show()
    app.exec()

