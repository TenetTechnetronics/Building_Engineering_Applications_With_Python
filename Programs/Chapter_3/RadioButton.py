from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QRadioButton, QLabel, QButtonGroup

class RadioButtonApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setGeometry(100, 100, 400, 200)
        self.setWindowTitle('QRadioButton Example')
        
    def initUI(self):
        # Create a layout
        layout = QVBoxLayout()

        # Create a QRadioButton
        radio1 = QRadioButton('Option 1')
        radio2 = QRadioButton('Option 2')
        radio3 = QRadioButton('Option 3')
                
        radio1.toggled.connect(self.onChange)
        radio2.toggled.connect(self.onChange)
        radio3.toggled.connect(self.onChange)

        # Do stop user from selecting option
        #radio3.setCheckable(False)
        # To disable radio button
        #radio2.setDisabled(True)
        
        # Add Radio button
        layout.addWidget(radio1)
        layout.addWidget(radio2)
        layout.addWidget(radio3)

         # Create a button group for the radio buttons
        self.button_group = QButtonGroup()
        self.button_group.addButton(radio1)
        self.button_group.addButton(radio2)
        self.button_group.addButton(radio3)


        # Add label to show state and value of checkbox
        self.label = QLabel()
        # set stylesheet
        self.label.setStyleSheet("font-size: 15px; font-weight: bold; color: Red;")
        layout.addWidget(self.label)
        self.setLayout(layout)
        
        # Set second option as selected by default
        radio2.setChecked(True)

    
    def onChange(self, value):
        print('Radio button: ', self.sender().text(), value)

        # Update selected radio button name and value in label when selected        
        if value == True:
            self.label.setText('Radio button: '+ self.sender().text() + ',  Value: '+ str(value))


if __name__ == '__main__':
    app = QApplication([])
    w = RadioButtonApp()
    w.show()
    app.exec()

