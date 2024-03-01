from PyQt6.QtWidgets import QApplication, QWidget, QStackedLayout, QPushButton, QVBoxLayout

# Initialize the application
app = QApplication([])

# Create a window
window = QWidget()      
window.setWindowTitle('Stacked Layout')
window.setMinimumWidth(400)
window.setMinimumHeight(400)

# Create a QVBoxLayout to hold the QStackedLayout and a Switch button
mainLayout = QVBoxLayout()

# Create the QStackedLayout
stackedLayout = QStackedLayout()

# Create widgets
widget1 = QPushButton('Page 1')
widget1.setStyleSheet('background-color: red;')
widget2 = QPushButton('Page 2')
widget2.setStyleSheet('background-color: green;')
widget3 = QPushButton('Page 3')
widget3.setStyleSheet('background-color: blue;')

# Add widgets to stacked layout
stackedLayout.addWidget(widget1)
stackedLayout.addWidget(widget2)
stackedLayout.addWidget(widget3)

totalViews = 3
# Function to switch between views
def onSwitchView():
    currentIndex = stackedLayout.currentIndex()
    if currentIndex < totalViews - 1:
        stackedLayout.setCurrentIndex(currentIndex + 1)
    else: 
        stackedLayout.setCurrentIndex(0)

# Button to switch views
switchButton = QPushButton('Switch View')
switchButton.clicked.connect(onSwitchView)

# Add layout and button to main layout
mainLayout.addLayout(stackedLayout)
mainLayout.addWidget(switchButton)

# Set main layout to window
window.setLayout(mainLayout)

# Show window
window.show()

# Start event loop
app.exec()
