from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton

# Initialize the application
app = QApplication([])

# Create the main window
window = QWidget()
window.setWindowTitle('QHBoxLayout')
window.setMinimumWidth(300)
window.setMinimumHeight(300)

# Create a QHBoxLayout
layout = QHBoxLayout()

# Create widgets 
button1 = QPushButton('Button 1')
button2 = QPushButton('Button 2')
button3 = QPushButton('Button 3')
button4 = QPushButton('Button 4')

# Add widgets to Layout
layout.addWidget(button1)
layout.addWidget(button2)
layout.addWidget(button3)
layout.addWidget(button4)

# Set the layout
window.setLayout(layout)

# Show the window
window.show()

# Run the application's event loop
app.exec()
