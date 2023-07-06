from PyQt6.QtWidgets import QApplication
from modules.GUI import MainWindow
from keras import models
import os

# fetching the current directory.
LOCAL_PATH = os.getcwd()
# print(LOCAL_PATH)

# loading a model to be used in the GUI.
WD_PATH =  os.path.abspath(LOCAL_PATH)
PATH_TRAINING = os.path.join(WD_PATH, "model_training")
model = models.load_model(
    os.path.join(PATH_TRAINING
                 ,"image_classifier_BvDtest_10artists.model"))

app = QApplication([])
window = MainWindow(LOCAL_PATH)
window.show()
app.exec()