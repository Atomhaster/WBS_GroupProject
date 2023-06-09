import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import tensorflow
from tensorflow import keras
from keras import datasets, layers, models
import os, random, csv
from keras.utils import to_categorical

from modules.painting import painting
from modules.database import database as db

# setting path variables for Working Directory and folder to save and load
#   models from.
WD_PATH =  os.path.split(os.path.abspath(__file__))[0]
PATH_TRAINING = os.path.join(WD_PATH, "model_training")



#### getting paintings from our db
# test_painting = painting("local DB")
# print(test_painting.artist_id)
# print(test_painting.id)
# imgplot = plt.imshow(test_painting.ndarray)
# plt.show()

# initializing the database object
gallery = db()

### How many pictures should be used per artist
SIZE_TRAINING = 190
SIZE_TESTING = 38
PIXEL_SIZE = 32

## creating arrays to hold the pictures taken from the DB
testing_images = np.zeros((10*SIZE_TESTING,PIXEL_SIZE,PIXEL_SIZE,3))
index_testing = 0
skip_count_testing = 0
training_images = np.zeros((10*SIZE_TRAINING,PIXEL_SIZE,PIXEL_SIZE,3))
index_training = 0
skip_count_training = 0
# creating the arrays to hold labels. In this case they are the artist ids.
testing_labels = np.zeros((10*SIZE_TESTING,1),dtype=int)
training_labels = np.zeros((10*SIZE_TRAINING,1),dtype=int)

# filling the arrays with picture arrays. They will be resized according
# to the pixel_size value
for i in range(1,11):
    ids = gallery.get_paintingids_from_artist(i)
    # random.seed(1983)
    random.shuffle(ids)
    ids_training = ids[ : SIZE_TRAINING]
    ids_testing = ids[SIZE_TRAINING : SIZE_TRAINING + SIZE_TESTING]
    ids_unused = ids[SIZE_TRAINING + SIZE_TESTING : ]
    for j in ids_testing:
        temp_p = painting("local DB", id=j[0])
        temp_p_res = cv.resize(temp_p.ndarray, dsize=(PIXEL_SIZE,PIXEL_SIZE)
                               ,interpolation=cv.INTER_CUBIC)
        if temp_p_res.shape == (PIXEL_SIZE,PIXEL_SIZE,3):
            testing_images[index_testing] = temp_p_res
            testing_labels[index_testing] = [temp_p.artist_id-1,]
            index_testing += 1
        else:
            skip_count_testing += 1
    # print("Testing images status")
    # print(index_testing)
    # print(skip_count_testing)
    for k in ids_training:
        temp_p = painting("local DB", id=k[0])
        temp_p_res = cv.resize(temp_p.ndarray, dsize=(PIXEL_SIZE,PIXEL_SIZE)
                               ,interpolation=cv.INTER_CUBIC)
        if temp_p_res.shape == (PIXEL_SIZE,PIXEL_SIZE,3):
            training_images[index_training] = temp_p_res
            training_labels[index_training] = [temp_p.artist_id-1,]
            index_training += 1
        else:
            skip_count_training += 1
    # print("Training images status")
    # print(index_training)
    # print(skip_count_training)

# ## dropping the last few array positions of testing images, which where 
# ## not filled.
testing_images = testing_images[:index_testing,:,:,:]
testing_labels = testing_labels[:index_testing,:]

# # the pixels on an image are rescaled from 0-255 to 0-1 
training_images, testing_images = training_images/255, testing_images/255 

# ## optional save and load the arrays.
# ## save ##
# with open("TEMP_arrays.npy", "wb") as f:
#     np.save(f, training_images)
#     np.save(f, training_labels)
#     np.save(f, testing_images)
# #     np.save(f, testing_labels)
# with open("TEMP_arrays.npy", "rb") as f:
#     training_images = np.load(f)
#     training_labels = np.load(f)
#     testing_images = np.load(f)
#     testing_labels = np.load(f)


# defining labels in a list
class_names = [i[1] for i in gallery.get_all_artists()]

# rand_ind = random.choices(list(range(1900)),k=9)
# print(rand_ind)

# print(class_names[(training_labels[rand_ind[0]][0])-1])
# img1 = training_images[rand_ind[0]]
# imgplot = plt.imshow(img1)
# plt.show()

# pos = 1
# for i in rand_ind:
#     plt.subplot(3,3,pos)
#     plt.xticks([])
#     plt.xticks([])
#     plt.imshow(training_images[i],cmap=plt.cm.binary)
#     plt.xlabel(class_names[(training_labels[i][0])-1])
#     pos += 1
# plt.show()

# reducing the amount of images fed to the model
# random numbers for index selection
rand_ind_tr = random.choices(list(range(1900)),k=200)
print(rand_ind_tr)
rand_ind_test = random.choices(list(range(360)),k=50)
print(rand_ind_test)
training_images = training_images[rand_ind_tr]
training_labels = training_labels[rand_ind_tr]
testing_images = testing_images[rand_ind_test]
testing_labels = testing_labels[rand_ind_test]

print(training_images.shape) # (200, 32, 32, 3)
print(testing_images.shape) # (50, 32, 32, 3)
print(testing_labels.shape) # (50,1)
print(training_labels.shape) # (200,1)

# Convert integer labels to one-hot encoded format
# training_labels = to_categorical(training_labels)
# testing_labels = to_categorical(testing_labels)

# Building the neural network
# adding convolutional layers
# Max Pooling 2D filters the result from the convolutional layer and
# simplifies it so that only the essential informations are left
# Flatten edit the input data so that it looks one dimensional
# Dense Layer is one where each neurons receives information from 
# all of the neurons of the previous layer
# model = models.Sequential()
# model.add(layers.Conv2D(16,(3,3),activation="relu"
#                         ,input_shape=(PIXEL_SIZE,PIXEL_SIZE,3)))
# # model.add(layers.MaxPool2D((2,2)))
# # model.add(layers.Conv2D(64,(3,3),activation="relu"))
# # model.add(layers.MaxPool2D((2,2)))
# # model.add(layers.Conv2D(64,(3,3),activation="relu"))
# model.add(layers.Flatten())
# # model.add(layers.Dense(64,activation="relu"))
# model.add(layers.Dense(11))

# model.compile(optimizer="adam",loss="sparse_categorical_crossentropy"
#               ,metrics=["accuracy"])
# model.fit(training_images,training_labels,batch_size = 1,epochs=10
#           , validation_data=(testing_images,testing_labels))

### FROM ChatGPT
model = models.Sequential()
# model.add(layers.Conv2D(16,(3,3),activation="relu",input_shape=(PIXEL_SIZE,PIXEL_SIZE,3)))
model.add(layers.Conv2D(16,(3,3),activation="relu"))
model.add(layers.MaxPooling2D((2,2)))

# Add more convolutional layers or any other layers here

model.add(layers.Flatten())
model.add(layers.Dense(1)) # Output layer with NUM_CLASSES neurons where NUM_CLASSES is number of classses present in dataset 
model.compile(optimizer="adam",loss="sparse_categorical_crossentropy",metrics=["accuracy"])

# Train model assuming training_labels and testing_labels are integer arrays instead one-hot encoded arrays 
history = model.fit(training_images,training_labels,batch_size=10,
                    epochs=10,
                    validation_data=(testing_images,testing_labels))

# In this step the model will be evaluated
loss,accuracy = model.evaluate(testing_images, testing_labels)
print(f"Loss: {loss}")
print(f"Accuracy: {accuracy}")

# model.save(os.path.join(PATH_TRAINING,"image_classifier_gallery1.model"))


###____________________________________________________________________________
### original from Mo with loaded example data set:
###____________________________________________________________________________

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


# # the pixels on an image are rescaled from 0-255 to 0-1 
# training_images, testing_images = training_images/255, testing_images/255 

# # defining labels in a list
# class_names = ["Plane","Car","Bird", "Cat","Deer","Dog","Frog","Horse","Ship","Truck"]

# # print(training_images.shape)
# item = 7
# print(training_labels[item])
# print(class_names[item])

# imgplot = plt.imshow(training_images[item])
# plt.show()

# print(type(training_images))

# print(training_labels[0])
# print(training_labels.shape)
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
# Max Pooling 2D filters the result from the convolutional layer and simplifies
# it so that only the essential informations are left
# Flatten edit the input data so that it looks one dimensional
# Dense Layer is one where each neurons receives information from all of the
# neurons of the previous layer
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
# epcohs seperate the training of data into different sessions,
# so that the same input data (images) are trained mutliple times 
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
