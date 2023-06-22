from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QHBoxLayout
from PyQt6.uic import load_ui
from PyQt6.QtGui import QCloseEvent
from ..modules import db_fill

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("GUI")
        self.ui = load_ui.loadUi("window11.ui", self)

        self.ui.painting.clicked.connect(self.painting_action) 
        self.ui.artist.clicked.connect(self.artist_action) 
        self.window1_opened=False
        self.window2_opened=False
        
#window1 = Painting-Window = window22.ui
#window2 = Artist-Window = window33.ui

#Painiting-Window öffnet sich            
    def painting_action(self):              
            if not self.window1_opened:
                window1 = paintingWindow()
                window1.show()       
                self.window1_opened = True
                window1.closeEvent = lambda event: self.window1_closed(event)          
#Painting-Window schließen, danach kann man wieder öffnen     
    def window1_closed(self,event):
        self.window1_opened = False    

#Artist-Window öffnet sich                 
    def artist_action(self):               
        if not self.window2_opened:
            window2=artistWindow()
            window2.show()
            self.window2_opened = True
            window2.closeEvent = lambda event: self.window2_closed(event)  
#Artist-Window schließen, danach kann man wieder öffnen     
    def window2_closed(self,event):
        self.window2_opened = False    


#Klasse für Painting-Window
class paintingWindow(QMainWindow):         
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Painting")
        self.ui = load_ui.loadUi("window22.ui", self)
    
#Klasse für Artist-Window
class artistWindow(QMainWindow):         
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Artist")
        self.ui = load_ui.loadUi("window33.ui", self)
      
app = QApplication([])
window = MainWindow()
window.show()
app.exec()   


