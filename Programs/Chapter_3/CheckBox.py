from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QCheckBox, QLabel
from PyQt6.QtCore import Qt

class CheckBoxApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setGeometry(100, 100, 400, 300)
        self.setWindowTitle('QCheckBox Example')
        
    def initUI(self):
        # Create a layout
        layout = QVBoxLayout()

        # Create a QCheckBox
        self.checkbox = QCheckBox('My CheckBox')
        # To set Tristate
        self.checkbox.setTristate(True)
        # stateChanged Event
        self.checkbox.stateChanged.connect(self.onStageChanged)
        
        # Add label to show state and value of checkbox
        self.label = QLabel()
        # set stylesheet
        self.label.setStyleSheet("font-size: 15px; font-weight: bold; color: Red;")
        layout.addWidget(self.checkbox, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.label, alignment=Qt.AlignmentFlag.AlignCenter)
        self.setLayout(layout)

        # Set default value for checkbox 
        self.checkbox.setCheckState(Qt.CheckState.Checked)
    
    def onStageChanged(self, value):
        self.label.setText('Checkbox State: '+ str(self.checkbox.checkState()) + ',  Value: '+ str(value))

if __name__ == '__main__':
    app = QApplication([])
    w = CheckBoxApp()
    w.show()
    app.exec()

