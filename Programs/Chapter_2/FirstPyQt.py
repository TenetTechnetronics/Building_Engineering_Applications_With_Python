from PyQt6.QtWidgets import QApplication, QWidget

#Create an Application
app = QApplication([])

#Create a Window
window = QWidget(windowTitle="Hello World!!")
window.show()

app.exec()