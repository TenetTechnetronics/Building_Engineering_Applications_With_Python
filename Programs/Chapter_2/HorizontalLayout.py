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

# Add widgets to Layout
layout.addWidget(button1)
layout.addWidget(button2)
layout.addWidget(button3)
layout.addWidget(button4)
layout.addWidget(button5)
layout.addWidget(button6)

#Set Spacing between widgets (spacing: int)
layout.setSpacing(60)

#Set marging for layout (left: int, top: int, right: int, bottom: int)
layout.setContentsMargins(10,10,250,250)
# Set the layout on the main window
window.setLayout(layout)

# Show the window
window.show()

# Run the application's event loop
app.exec()
