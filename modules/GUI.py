from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtGui import QPixmap, QImage
from modules.painting import painting
from modules.artist import artist
import numpy as np
from erste_GUI.windows_stacked_01 import Ui_MainWindow

import cv2 as cv
from wikipedia import wikipedia

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, local_path, classification_model):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("GUI")
        
        self.user_guess = None
        self.painting_in_question = None
        self.class_model = classification_model
        
        self.local_path = local_path + "\\erste_GUI\\"
        self.pushButton_start_1.clicked.connect(self.start) 
        self.pushButton_start2.clicked.connect(self.reset)
        self.pushButton.clicked.connect(self.drop_selected)
        
        self.machine_answer.setWordWrap(True)
        
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
        
        self.drop_down_artist.setItemText(0, "Vincent van Gogh")
        self.drop_down_artist.setItemText(1, "Pablo Picasso")
        self.drop_down_artist.addItem("Pierre Auguste Renoir")
        self.drop_down_artist.addItem("Francisco de Goya")
        self.drop_down_artist.addItem("Alfred Sisley")
        self.drop_down_artist.addItem("Marc Chagall")
        self.drop_down_artist.addItem("Edgar Degas")
        self.drop_down_artist.addItem("Rembrandt")
        self.drop_down_artist.addItem("Titian")
        self.drop_down_artist.addItem("Paul Gougain")
        
        # example_painting2 = self.load_painting(artist_name="Vincent van Gogh")
        # self.painting2.setPixmap(example_painting2)
       
    def exchange_random(self, image_obj, text_obj=None, return_painting= False):
        if return_painting:
            example_painting1, artist_name, painting = self.load_painting(return_painting=return_painting)
        else:
            example_painting1, artist_name = self.load_painting()
        if text_obj:
            text_obj.setText(artist_name)
        image_obj.setPixmap(example_painting1)
        if return_painting:
            return painting
    
    def start(self):
        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(0)
    
    def reset(self):
        self.painting_in_question = self.exchange_random(self.painting_image_random
                                                        ,return_painting=True)
        self.stackedWidget_2.setCurrentIndex(0)
        self.drop_down_artist.setCurrentIndex(0)
                
    def drop_selected(self):
        self.stackedWidget_2.setCurrentIndex(1)
        # self.user_guess =  self.drop_down_artist.currentIndex()
        self.user_guess =  self.drop_down_artist.currentText()
        print(self.user_guess)
        # artist_user_sel = artist(id=self.user_guess)
        new_text = "Your guess is: " + self.user_guess
        
        artist_true = artist(id=self.painting_in_question.artist_id)
        # new_text = new_text + "\n" + "The correct answer is: " + str(self.painting_in_question.artist_id)
        new_text = new_text + "\n" + "The correct answer is: " + artist_true.name
        
        ## getting machine predictions and displaying answer
        machine_pred = self.model_prediction(self.painting_in_question)
        new_text = (new_text + "\n" 
                    + "The model prediction is: " 
                    + machine_pred.name)
        
        ## information from the DB of the artist:
        new_text = (new_text + "\n\n" + str(artist_true.name) 
                    + ", * " + str(artist_true.birth)
                    + ", † " + str(artist_true.death))
        
        ## wiki entry for the artist:
        wiki = wikipedia.summary((artist_true.name + "Painter"), sentences = 1)
        new_text = new_text + "\n" +  wiki
        
        # setting the text in the object and changing font size
        self.machine_answer.setText(new_text)
        ma_font = self.machine_answer.font()
        ma_font.setPointSize(12)
        self.machine_answer.setFont(ma_font)
    
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
        
    def model_prediction(self, painting, PIXEL_SIZE=256):
        test_ndarray = cv.resize(painting.ndarray, dsize=(PIXEL_SIZE,PIXEL_SIZE)
                               ,interpolation=cv.INTER_CUBIC)
        test_ndarray = test_ndarray/255
        temp_array = np.zeros((1,PIXEL_SIZE,PIXEL_SIZE,3))
        print(temp_array.shape)
        temp_array[0] = test_ndarray
        prediction = self.class_model.predict(temp_array)
        index = np.argmax(prediction)
        artist_temp = artist(id= index+1)
        return artist_temp
