from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QHBoxLayout

from PyQt6.uic import load_ui

class SecondWindow(QMainWindow):
    def __init__(self, master=None) -> None:
        super().__init__(master) 
        self.setWindowTitle("mainwindow_1905_22")
        self.container = QWidget()
        self.main_layout = QHBoxLayout()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("GUI")
        self.ui = load_ui.loadUi("erste_idee.ui", self)
        # zugriff auf die Oberfläche (self.ui), objectName aus der ui, signal= clicked
        # connect; (slot) in diesem fall ein methodenobjekt
        self.ui.painting.clicked.connect(self.action) #zeile verstehen!
    
        self.container = QWidget()
        self.main_layout = QHBoxLayout()    
    
        self.button = QPushButton("Open new Window")
        self.button.clicked.connect(self.on_activate)
        
        self.setCentralWidget(self.button)    

    def action(self):
        self.new_window = SecondWindow()
        self.new_window.show()
        print("Ausgabe")
      
      
app = QApplication([])
window = MainWindow()
window.show()
app.exec()   