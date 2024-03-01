from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QTreeWidget, QTreeWidgetItem, QPushButton
from PyQt6.QtCore import Qt

class TreeWidgetApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setGeometry(100, 100, 400, 400)
        self.setWindowTitle('TreeWidget Example')
        
    def initUI(self):
        # Create a layout
        layout = QVBoxLayout()
        
        # Create tree widget
        self.tree = QTreeWidget()

        # Set number of columns
        self.tree.setColumnCount(2)
        # Set column headers
        self.tree.setHeaderLabels(["Car Company", "Car Model"])

        # Data for tree
        data = {
            "Honda": ["Accord", "Pilot", "CR-V"],
            "Toyota": ["Camry", "Rav4"],
            "Hyundai": ["Accent"],
            "Subaru": ["Outback", "Crosstrek", "Forester"]
        }

        # Populate tree widget with data
        for department, employees in data.items():
            department_item = QTreeWidgetItem(self.tree)
            department_item.setText(0, department)
            
            for employee in employees:
                employee_item = QTreeWidgetItem(department_item)
                employee_item.setText(1, employee)

        # Show the tree widget
        self.tree.show()
        self.tree.sortByColumn(1, Qt.SortOrder.AscendingOrder)
        layout.addWidget(self.tree)

        hLayout = QHBoxLayout()
        button1 = QPushButton("Expand")
        button2 = QPushButton("Collapse")
        button1.clicked.connect(self.expand)
        button2.clicked.connect(self.collapse)
        hLayout.addWidget(button1)
        hLayout.addWidget(button2)

        layout.addLayout(hLayout)
        self.setLayout(layout)

    def expand(self):
        self.tree.expandAll()
    
    def collapse(self):
        self.tree.collapseAll()
    
if __name__ == '__main__':
    app = QApplication([])
    w = TreeWidgetApp()
    w.show()
    app.exec()

