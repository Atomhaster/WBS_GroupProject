from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QHBoxLayout

from PyQt6.uic import load_ui

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("GUI")
        self.ui = load_ui.loadUi("erste_idee.ui", self)
        # zugriff auf die Oberfläche (self.ui), objectName aus der ui, signal= clicked
        # connect; (slot) in diesem fall ein methodenobjekt
        self.ui.painting.clicked.connect(self.action) #zeile verstehen!
      

    def action(self):
        print("Neues Fenster öffnen")
      
      
app = QApplication([])
window = MainWindow()
window.show()
app.exec()   