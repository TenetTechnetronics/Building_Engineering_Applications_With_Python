import os
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QTabWidget, QVBoxLayout, QLabel, QPushButton
from PyQt6.QtGui import QIcon

# local machine repository path
path = os.environ.get('SampleProgram')

class TabWidgetApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 400, 400)
        self.setWindowTitle('TabWidget Example')
        self.initUI()
        
    def initUI(self):
        # Create Tab widget
        self.tabWidget = QTabWidget()
        self.addTabs()

        # Enable Tab rearrange
        self.tabWidget.setMovable(True)
        self.setCentralWidget(self.tabWidget)
    
    def addTabs(self):
        tab1 = QWidget()
        layout1 = QVBoxLayout()
        label1 = QLabel('This is the content of Tab 1.')
        layout1.addWidget(label1)
        tab1.setLayout(layout1)

        button1 = QPushButton("Add")
        button2 = QPushButton("Remove")
        button1.clicked.connect(self.addTab)
        button2.clicked.connect(self.removeTab)
        layout1.addWidget(button1)
        layout1.addWidget(button2)

        # Add tab to the tab widget
        self.tabWidget.addTab(tab1, 'Tab 1')
        
        tab2 = QWidget()
        layout2 = QVBoxLayout()
        label2 = QLabel('This is the content of Tab 2.')
        layout2.addWidget(label2)
        tab2.setLayout(layout2)
        # Tab icon is optional.
        # Create icon with image page
        self.icon = QIcon(path + 'assets/images/save_icon.png')
		        
        # Add tab to the tab widget
        self.tabWidget.addTab(tab2, 'Tab 2')
        self.tabWidget.setTabIcon(1, self.icon)

        tab3 = QWidget()
        layout3 = QVBoxLayout()
        label3 = QLabel('This is the content of Tab 3.')
        layout3.addWidget(label3)
        tab3.setLayout(layout3)
        
        # Add tab to the tab widget
        self.tabWidget.addTab(tab3, 'Tab 3')
        # Set icon for Tab
        self.tabWidget.setTabIcon(2, self.icon)

    def addTab(self):
        tabCount = self.tabWidget.count()
        tab = QWidget()
        layout = QVBoxLayout()
        label = QLabel('This is the content of Tab ' + str(tabCount + 1))
        layout.addWidget(label)
        tab.setLayout(layout)
        # Add Tab at index
        self.tabWidget.insertTab(tabCount, tab, 'Tab ' + str(tabCount + 1))
        self.tabWidget.setTabIcon(tabCount, self.icon)

    def removeTab(self):
        if self.tabWidget.count() > 1: 
            # Remove Tab at index
            self.tabWidget.removeTab(1)

if __name__ == '__main__':
    app = QApplication([])
    w = TabWidgetApp()
    w.show()
    app.exec()

