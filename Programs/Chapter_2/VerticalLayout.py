from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton

# Initialize the PyQt application
app = QApplication([])

# Create the main window
mainWindow = QWidget()
mainWindow.setWindowTitle("QVBoxLayout")
mainWindow.setMinimumWidth(300)
mainWindow.setMinimumHeight(300)
# Create a QVBoxLayout instance
layout = QVBoxLayout()

# Create and add widgets to the layout in one line
layout.addWidget(QPushButton("Button 1"))
layout.addWidget(QPushButton("Button 2"))
layout.addWidget(QPushButton("Button 3"))
layout.addWidget(QPushButton("Button 4"))

# Set the layout 
mainWindow.setLayout(layout)

# Display the main window
mainWindow.show()  

# Start the event loop
app.exec()
