from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton

# Initialize the application
app = QApplication([])

# Create the main window
window = QWidget()
window.setWindowTitle('QHBoxLayout')
window.setMinimumWidth(800)
window.setMinimumHeight(600)

# Create a QHBoxLayout instance
layout = QHBoxLayout()

# Create widgets 
button1 = QPushButton('Button 1')
button2 = QPushButton('Button 2')
button3 = QPushButton('Button 3')
button4 = QPushButton('Button 4')
button5 = QPushButton('Button 5')
button6 = QPushButton('Button 6')
button7 = QPushButton('Button 7')
button8 = QPushButton('Button 8')

# Add widgets to Layout
layout.addWidget(button1)
layout.addWidget(button2)
layout.addWidget(button3)
layout.addWidget(button4)
layout.addWidget(button5)
layout.addWidget(button6)
layout.addWidget(button7)
layout.addWidget(button8)

# Set the layout on the main window
window.setLayout(layout)

# Show the window
window.show()

# Run the application's event loop
app.exec()
