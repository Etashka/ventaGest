
#esta es la parte de "todo" pero para que se vea en una aplicación de escritorio porque la hice en html
import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Web Browser")
        self.setGeometry(100, 100, 800, 600)

        self.web_view = QWebEngineView()
        self.web_view.load(QUrl.fromLocalFile(r'C:\\Users\\nara\\Desktop\\Atento 2024\\Proyectos\\Taskify\\to_do\\todo.html')) 
        self.setCentralWidget(self.web_view)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())