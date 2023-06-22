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

class MainWindow(QMainWindow):
    def __init__(self, local_path):
        super().__init__()
        self.setWindowTitle("GUI")
        self.local_path = local_path + "\\erste_GUI\\"
        self.ui = load_ui.loadUi(self.local_path + "window11.ui", self)
        self.ui.painting.clicked.connect(self.painting_action) 
        self.ui.artist.clicked.connect(self.artist_action) 
        self.window1_opened=False
        self.window2_opened=False
        
        example_painting1 = painting(db_type="remote DB",artist_name="Pablo Picasso")
        # print(example_painting1.ndarray.shape[1]
        #                , example_painting1.ndarray.shape[0])
        # print(example_painting1.ndarray.dtype)
        # print(np.dtype('<i4').byteorder)
        # img_fe = plt.imshow(example_painting1.ndarray)
        # plt.show()
        qimg1 = QImage(example_painting1.ndarray
                       , example_painting1.ndarray.shape[1]
                       , example_painting1.ndarray.shape[0]
                       , example_painting1.ndarray.shape[1] * 3
                       , QImage.Format.Format_RGB888
                       )
        qpixmap1 = QPixmap.fromImage(qimg1)
        # qpixmap1 = qpixmap1.scaled(100,100)
        p1 = self.ui.findChild(QLabel, "painting1")
        p1 = p1.setPixmap(qpixmap1)
        
        
        example_painting2 = painting(db_type="remote DB",artist_name="Vincent van Gogh")
        qimg2 = QImage(example_painting2.ndarray
                       , example_painting2.ndarray.shape[1]
                       , example_painting2.ndarray.shape[0]
                       , example_painting2.ndarray.shape[1] * 3
                       ,QImage.Format.Format_RGB888
                       )
        qpixmap2 = QPixmap.fromImage(qimg2)
        # qpixmap2 = qpixmap2.scaled(100,100)
        p2 = self.ui.findChild(QLabel, "painting2")
        p2.setPixmap(qpixmap2)
        
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