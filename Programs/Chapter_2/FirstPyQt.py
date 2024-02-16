from PyQt6.QtWidgets import QApplication, QWidget

#create an Application
app = QApplication([])

#create a window
window = QWidget(windowTitle="Hello World!!")
window.show()

app.exec()