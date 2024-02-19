from PyQt6.QtWidgets import QApplication, QWidget, QStackedLayout, QPushButton, QVBoxLayout

# Initialize the application
app = QApplication([])

# Create a window
window = QWidget()

# Create a QVBoxLayout to hold the QStackedLayout and a button for switching views
mainLayout = QVBoxLayout()

# Create the QStackedLayout
stackedLayout = QStackedLayout()

# Create widgets to add to the stacked layout
widget1 = QPushButton('View 1')
widget2 = QPushButton('View 2')

# Add widgets to the stacked layout
stackedLayout.addWidget(widget1)
stackedLayout.addWidget(widget2)

# Function to switch between views
def switch_view():
    currentIndex = stackedLayout.currentIndex()
    newIndex = 1 if currentIndex == 0 else 0  # Switch between 0 and 1
    stackedLayout.setCurrentIndex(newIndex)

# Button to switch views
switchButton = QPushButton('Switch View')
switchButton.clicked.connect(switch_view)

# Add the stacked layout and switch button to the main layout
mainLayout.addLayout(stackedLayout)
mainLayout.addWidget(switchButton)

# Set the main layout to the window
window.setLayout(mainLayout)
# Display the window
window.show()

# Start the event loop
app.exec()
