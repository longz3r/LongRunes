import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox


class ExampleApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('PyQt5 Example')
        self.setGeometry(100, 100, 300, 200)

        button = QPushButton('Click Me', self)
        button.setGeometry(100, 80, 100, 30)
        button.clicked.connect(self.showMessageBox)

    def showMessageBox(self):
        QMessageBox.information(self, 'Message', 'Button Clicked!')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    sys.exit(app.exec_())
