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
from erste_GUI.windows_stacked_01 import Ui_MainWindow
from wikipedia import wikipedia

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, local_path):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("GUI")
        
        self.user_guess = None
        self.painting_in_question = None
        
        self.local_path = local_path + "\\erste_GUI\\"
        self.pushButton_start_1.clicked.connect(self.start) 
        self.pushButton_start2.clicked.connect(self.reset)
        self.dop_down_artist.currentIndexChanged.connect(self.drop_selected)
        
        # example_painting1, artist_name = self.load_painting()
        # self.painting_image1.setPixmap(example_painting1)
        # self.painting_image1_text.setText(artist_name)
        self.exchange_random(self.painting_image1,self.painting_image1_text)
        self.exchange_random(self.painting_image2,self.painting_image2_text)
        self.exchange_random(self.painting_image3,self.painting_image3_text)
        self.exchange_random(self.painting_image4,self.painting_image4_text)
        
        self.painting_in_question = self.exchange_random(self.painting_image_random
                                                        ,self.painting_image4_text
                                                        ,return_painting=True)
        
        self.dop_down_artist.setItemText(0, "Vincent van Gogh")
        self.dop_down_artist.setItemText(1, "Pablo Picasso")
        self.dop_down_artist.addItem("Pierre Auguste Renoir")
        self.dop_down_artist.addItem("Francisco de Goya")
        self.dop_down_artist.addItem("Alfred Sisley")
        self.dop_down_artist.addItem("Marc Chagall")
        self.dop_down_artist.addItem("Edgar Degas")
        self.dop_down_artist.addItem("Rembrandt")
        self.dop_down_artist.addItem("Titian")
        self.dop_down_artist.addItem("Paul Gougain")
        
        # example_painting2 = self.load_painting(artist_name="Vincent van Gogh")
        # self.painting2.setPixmap(example_painting2)
       
    def exchange_random(self, image_obj, text_obj=None, return_painting= False):
        if return_painting:
            example_painting1, artist_name, painting = self.load_painting(return_painting=return_painting)
        else:
            example_painting1, artist_name = self.load_painting()
        if text_obj:
            image_obj.setPixmap(example_painting1)
        text_obj.setText(artist_name)
        if return_painting:
            return painting
    
    def start(self):
        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(0)
    
    def reset(self):
        self.exchange_random(self.painting_image_random,self.painting_image4_text)
        self.stackedWidget_2.setCurrentIndex(0)
        
    def drop_selected(self):
        self.stackedWidget_2.setCurrentIndex(1)
        # self.user_guess =  self.dop_down_artist.currentIndex()
        self.user_guess =  self.dop_down_artist.currentText()
        print(self.user_guess)
        # artist_user_sel = artist(id=self.user_guess)
        new_text = "Your guess is: " + self.user_guess
        
        artist_true = artist(id=self.painting_in_question.artist_id)
        new_text = new_text + "\n" + "The correct answer is: " + str(self.painting_in_question.artist_id)
        # new_text = new_text + "\n" + "The correct answer is: " + artist_true.name
        
        self.machine_answer.setText(new_text)
    
    def load_painting(self,artist_name=None, id=None, return_painting= False):
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
        artist_temp = artist(id= painting_temp.artist_id)
        if return_painting:
            return qpixmap2, artist_temp.name, painting_temp
        else:
            return qpixmap2, artist_temp.name
