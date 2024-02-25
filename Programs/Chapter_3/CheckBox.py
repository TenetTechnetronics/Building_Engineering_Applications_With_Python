from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QCheckBox
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
        self.checkbox.setCheckState(Qt.CheckState.Checked)
        # To set Tristate
        self.checkbox.setTristate(True)
        # stateChanged Event
        self.checkbox.stateChanged.connect(self.onStageChanged)
        # Add LineEdit
        layout.addWidget(self.checkbox, alignment=Qt.AlignmentFlag.AlignCenter)

        self.setLayout(layout)
    
    def onStageChanged(self, value):
        print('Stage Changed ', value, self.checkbox.checkState())

if __name__ == '__main__':
    app = QApplication([])
    w = CheckBoxApp()
    w.show()
    app.exec()

