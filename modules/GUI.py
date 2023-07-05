from PyQt6.QtWidgets import (QMainWindow, QApplication, QPushButton
                             , QWidget, QHBoxLayout, QLabel)
from PyQt6.uic import load_ui
from PyQt6.QtGui import QCloseEvent
from PyQt6.QtGui import QPixmap, QImage
from modules.painting import painting
from modules.artist import artist
import numpy as np
from sys import getsizeof
import matplotlib.pyplot as plt
from erste_GUI.window11 import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, local_path):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("GUI")
        self.local_path = local_path + "\\erste_GUI\\"
        self.ui = load_ui.loadUi(self.local_path + "window11.ui", self)
        self.ui.painting.clicked.connect(self.painting_action) 
        self.ui.artist.clicked.connect(self.artist_action) 
        self.window1_opened=False
        self.window2_opened=False
        
        example_painting1 = self.load_painting(artist_name="Pablo Picasso")
        self.painting1.setPixmap(example_painting1)
        
        example_painting2 = self.load_painting(artist_name="Vincent van Gogh")
        self.painting2.setPixmap(example_painting2)
        
#window1 = Painting-Window = window22.ui
#window2 = Artist-Window = window33.ui

#Painiting-Window öffnet sich            
    def painting_action(self):              
            if not self.window1_opened:
                window1 = paintingWindow(self.local_path)
                window1.show()       
                self.window1_opened = True
                window1.closeEvent = lambda event: self.window1_closed(event)          
#Painting-Window schließen, danach kann man wieder öffnen     
    def window1_closed(self,event):
        self.window1_opened = False    

#Artist-Window öffnet sich                 
    def artist_action(self):               
        if not self.window2_opened:
            window2=artistWindow(self.local_path)
            window2.show()
            self.window2_opened = True
            window2.closeEvent = lambda event: self.window2_closed(event)  
#Artist-Window schließen, danach kann man wieder öffnen     
    def window2_closed(self,event):
        self.window2_opened = False   
    
    def load_painting(self,artist_name=None, id=None):
        if id:
            painting_temp = painting(db_type="local DB",id=id)
        elif artist_name:
            painting_temp = painting(db_type="local DB",artist_name=artist_name)
        else:
            painting_temp = painting(db_type="local DB")
        qimg2 = QImage(painting_temp.ndarray
                       , painting_temp.ndarray.shape[1]
                       , painting_temp.ndarray.shape[0]
                       , painting_temp.ndarray.shape[1] * 3
                       ,QImage.Format.Format_RGB888
                       )
        qpixmap2 = QPixmap.fromImage(qimg2)
        return qpixmap2


#Klasse für Painting-Window
class paintingWindow(QMainWindow):         
    def __init__(self, local_path):
        super().__init__()
        self.local_path = local_path
        self.setWindowTitle("Painting")
        self.ui = load_ui.loadUi(self.local_path + "window22.ui", self)
        

#Klasse für Artist-Window
class artistWindow(QMainWindow):         
    def __init__(self, local_path):
        super().__init__()
        self.local_path = local_path
        self.setWindowTitle("Artist")
        self.ui = load_ui.loadUi(self.local_path +  "window33.ui", self)