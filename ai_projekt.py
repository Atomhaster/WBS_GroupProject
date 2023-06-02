from PyQt6.QtWidgets import QApplication
from modules.GUI import MainWindow
import os

LOCAL_PATH = os.getcwd()

print(LOCAL_PATH)


app = QApplication([])
window = MainWindow(LOCAL_PATH)
window.show()
app.exec()   