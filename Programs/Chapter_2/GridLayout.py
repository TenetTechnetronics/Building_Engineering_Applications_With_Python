from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton

# Initialize the application
app = QApplication([])

# Create a window
window = QWidget()
window.setWindowTitle('QGridLayout')
window.setMinimumWidth(400)
window.setMinimumHeight(400)

# Create a QGridLayout
layout = QGridLayout()

# Create widgets 
button1 = QPushButton('Button 1')
button2 = QPushButton('Button 2')
button3 = QPushButton('Button 3')
button4 = QPushButton('Button 4')
button5 = QPushButton('Button 5')
button6 = QPushButton('Button 6')
button7 = QPushButton('Button 7')


# Add widgets to the layout at specified positions
layout.addWidget(button1, 0, 0) # Arguments row, column
layout.addWidget(button2, 0, 1, 1, 2) # Arguments row, column, rowSpan, columnSpan
layout.addWidget(button3, 0, 3) # Arguments row, column
layout.addWidget(button4, 1, 0, 1, 2) # Arguments row, column, rowSpan, columnSpan
layout.addWidget(button5, 1, 2) # Arguments row, column
layout.addWidget(button6, 1, 3) # Arguments row, column
layout.addWidget(button7, 2, 0, 1, 4) # Arguments row, column, rowSpan, columnSpan

# Apply the layout to the window
window.setLayout(layout)

# Display the window
window.show()

# Start the application's event loop
app.exec()
