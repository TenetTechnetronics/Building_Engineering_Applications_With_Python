from PyQt6.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout, QHBoxLayout, QLabel

class StyleButton(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Style Button")
        self.setGeometry(200, 200, 400, 300)
        mainLayout = QVBoxLayout()
        
        layout = QHBoxLayout()
        button1 = QPushButton("Cancel")
        # Set Style For Button
        button1.setStyleSheet(
            "border: 2px solid #ff00c4;"
            "color: #ff00c4;"
            "font-weight: bold;"
            "padding: 10px;"
            "text-align: center;"
            "font-size: 20px;"
            "margin: 4px 2px;"
            "border-radius: 12px;"
        )

        layout.addWidget(button1)
        mainLayout.addLayout(layout)

        button2 = QPushButton("Login")
        # Set Style For Button
        button2.setStyleSheet(
            "background-color: #ff00c4;"
            "color: white;"
            "font-weight: bold;"
            "padding: 10px;"
            "text-align: center;"
            "font-size: 20px;"
            "margin: 4px 2px;"
            "border-radius: 12px;"
        )
        layout.addWidget(button2)

        self.setLayout(mainLayout)
    
if __name__ == "__main__":
    app = QApplication([])
    window = StyleButton()
    window.show()
    app.exec()
