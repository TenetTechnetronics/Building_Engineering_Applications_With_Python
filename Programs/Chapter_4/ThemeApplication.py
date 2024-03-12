from PyQt6.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit
from PyQt6.QtCore import QRect

class StyleButton(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Style Button")
        self.setGeometry(200, 200, 400, 400)
        self.mainLayout = QVBoxLayout()
        
        layout = QHBoxLayout()
        lightBtn = QPushButton("Light Theme")
        lightBtn.setFixedWidth(100)
        lightBtn.setFixedHeight(30)
        layout.addWidget(lightBtn)

        darkBtn = QPushButton("Dark Theme")
        darkBtn.setFixedWidth(100)
        darkBtn.setFixedHeight(30)
        layout.addWidget(darkBtn)

        self.mainLayout.addLayout(layout)
        
        self.createLoginWidget()
        self.setLayout(self.mainLayout)
    
    def createLoginWidget(self):
        loginWidget = QWidget()
        loginWidget.setStyleSheet("background-color:green;")
        self.mainLayout.addWidget(loginWidget)
        loginLayout = QVBoxLayout()
        nameLabel = QLabel("User Name:")
        passwordLabel = QLabel("Password:")
        self.userName = QLineEdit()
        self.password = QLineEdit()
        loginLayout.addWidget(nameLabel)
        loginLayout.addWidget(self.userName)
        loginLayout.addWidget(passwordLabel)
        loginLayout.addWidget(self.password)


        btnLayout = QHBoxLayout()
        cancelBtn = QPushButton("Cancel")
        btnLayout.addWidget(cancelBtn)
        loginBtn = QPushButton("Login")
        btnLayout.addWidget(loginBtn)
        
        loginLayout.addLayout(btnLayout)

        loginWidget.setLayout(loginLayout)


if __name__ == "__main__":
    app = QApplication([])
    window = StyleButton()
    window.show()
    app.exec()
