from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QTableWidget, QTableWidgetItem, QPushButton

class TableWidgetApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setGeometry(100, 100, 400, 400)
        self.setWindowTitle('TableWidget Example')
        
    def initUI(self):
        # Create a layout
        layout = QVBoxLayout()
        
        self.table = QTableWidget(5, 3)
        self.table.setHorizontalHeaderLabels(["Name", "Email", "Phone"])
        
        # Data for Table
        data = [
            {"name":"Rob", "email":"ram@gmail.com", "phone": "248-789-4566"},  
            {"name":"Bob", "email":"bob32@gmail.com", "phone": "457-789-4566"},  
            {"name":"Tom", "email":"tom87@gmail.com", "phone": "248-343-6789"},
            {"name":"Kim", "email":"kim65@gmail.com", "phone": "487-568-4213"},
            {"name":"Sam", "email":"sam98@gmail.com", "phone": "248-864-5677"}
        ]

        # SetItem to table
        for index, item in enumerate(data):
            self.table.setItem(index, 0, QTableWidgetItem(item['name']))
            self.table.setItem(index, 1, QTableWidgetItem(item['email']))
            self.table.setItem(index, 2, QTableWidgetItem(item['phone']))

        layout.addWidget(self.table)
        hLayout = QHBoxLayout()
        button1 = QPushButton("Add")
        button2 = QPushButton("Remove")
        button1.clicked.connect(self.addItem)
        button2.clicked.connect(self.removeItem)
        hLayout.addWidget(button1)
        hLayout.addWidget(button2)

        layout.addLayout(hLayout)
        self.setLayout(layout)

    def addItem(self):
        index = self.table.rowCount()
        self.table.insertRow(index)
        self.table.setItem(index, 0, QTableWidgetItem('name' + str(index)))
        self.table.setItem(index, 1, QTableWidgetItem('email' + str(index)))
        self.table.setItem(index, 2, QTableWidgetItem('phone' + str(index)))
    
    def removeItem(self):
        self.table.removeRow(self.table.currentRow())
    
if __name__ == '__main__':
    app = QApplication([])
    w = TableWidgetApp()
    w.show()
    app.exec()

