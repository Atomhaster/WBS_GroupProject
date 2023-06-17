import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
# import tensorflow
from tensorflow import keras
from keras import datasets, layers, models
import os, random, csv

from modules.painting import painting
from modules.database import database as db

# setting path variables for Working Directory and folder to save and load
#   models from.
WD_PATH =  os.path.split(os.path.abspath(__file__))[0]
PATH_TRAINING = os.path.join(WD_PATH, "model_training")

# Dataset from Keras wird importiert und aufgeteilt in training- und testing images/labels
# (training_images, training_labels), (testing_images, testing_labels) = datasets.cifar10.load_data()

### exploring datashape #####
# print(type(training_images))
# print(training_images.ndim)
# print(training_images.shape)
# print(testing_images.shape)
# print(training_images[1].shape)
# img1 = training_images[1]
# imgplot = plt.imshow(img1)
# plt.show()
# print(training_images[0][0])


#### getting paintings from our db
# test_painting = painting("local DB")
# print(test_painting.artist_id)
# print(test_painting.id)
# imgplot = plt.imshow(test_painting.ndarray)
# plt.show()

gallery = db()
# print(gallery.get_artist_id("Pablo Picasso"))

SIZE_TRAINING = 190
SIZE_TESTING = 38


testing_images = np.zeros((10*SIZE_TRAINING,500,500,3))
index_testing = 0
for i in range(6,7):
    ids = gallery.get_paintingids_from_artist(i)
    random.seed(1983)
    random.shuffle(ids)
    ids_training = ids[ : SIZE_TRAINING]
    ids_testing = ids[SIZE_TRAINING : SIZE_TRAINING + SIZE_TESTING]
    ids_unused = ids[SIZE_TRAINING + SIZE_TESTING : ]
    for j in ids_testing:
        temp_p = painting("local DB", id=j[0])
        temp_p_res = cv.resize(temp_p.ndarray, dsize=(500,500)
                               ,interpolation=cv.INTER_CUBIC)
        testing_images[index_testing] = temp_p_res
        

print(testing_images.shape)






# # the pixels on an image are rescaled from 0-255 to 0-1 
# training_images, testing_images = training_images/ 255, testing_images/255 

# # defining labels in a list
# class_names = ["Plane","Car","Bird", "Cat","Deer","Dog","Frog","Horse","Ship","Truck"]

# # print(training_images.shape)
# item = 7
# print(training_labels[item])
# print(class_names[item])

# imgplot = plt.imshow(training_images[item])
# plt.show()

# print(type(training_images))

# for i in range(16):
#     plt.subplot(4,4,i+1)
#     plt.xticks([])
#     plt.xticks([])
#     plt.imshow(training_images[i],cmap=plt.cm.binary)
#     plt.xlabel(class_names[training_labels[i][0]])
    
# plt.show()

# reducing the amount of images fed to the model
# training_images = training_images[:40000]
# training_labels = training_labels[:40000]
# testing_images = testing_images[:8000]
# testing_labels = testing_labels[:8000]


# Building the neural network
# adding convolutional layers
# Max Pooling 2D filters the result from the convolutional layer and simplifies it so that only the essential informations are left
# Flatten edit the input data so that it looks one dimensional
# Dense Layer is one where each neurons receives information from all of the neurons of the previous layer
# model = models.Sequential()
# model.add(layers.Conv2D(32,(3,3),activation="relu",input_shape=(32,32,3)))
# model.add(layers.MaxPool2D((2,2)))
# model.add(layers.Conv2D(64,(3,3),activation="relu"))
# model.add(layers.MaxPool2D((2,2)))
# model.add(layers.Conv2D(64,(3,3),activation="relu"))
# model.add(layers.Flatten())
# model.add(layers.Dense(64,activation="relu"))
# model.add(layers.Dense(10,activation="softmax"))

# the compiler checks for format errors, and defines the loss function, the optimizer or learning rate, and the metrics
# The optimizer finds the perfect weights until no more numerical improvement can be achieved
# model.compile(optimizer="adam",loss="sparse_categorical_crossentropy",metrics=["accuracy"])

# Here the data will be fed to the model
# epcohs seperate the training of data into different sessions, so that the same input data (images) are trained mutliple times 
# model.fit(training_images,training_labels,batch_size = 1,epochs=10, validation_data=(testing_images,testing_labels))


# In this step the model will be evaluated
# loss,accuracy = model.evaluate(testing_images, testing_labels)
# print(f"Loss: {loss}")
# print(f"Accuracy: {accuracy}")

# model.save(os.path.join(PATH_TRAINING,"image_classifier3.model"))

# model = models.load_model(os.path.join(PATH_TRAINING,"image_classifier3.model"))

# path = r"G:\WBS - Data Science mit Python\WBS_GroupProject\classification\plane.jpg"
# img = cv.imread(path)

# # # converting the image from BGR to RGB 
# img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

# plt.imshow(img, cmap=plt.cm.binary)

# # # and finally a prediction will be made
# prediction = model.predict(np.array([img])/ 255)

# index = np.argmax(prediction)

# print(f"Prediction is {class_names[index]}")
