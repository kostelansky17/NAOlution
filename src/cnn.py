import array
import numpy as np
import tensorflow as tf
from keras import backend as K
from keras.models import Sequential
from keras.preprocessing import keras_image
from keras.activations import relu, tanh
from keras.initializers import random_normal
from keras.layers.core import Dense, Flatten, Dropout
from keras.layers.convolutional import Conv2D, MaxPooling2D


"""
Creates Convolutional Neural Network with randomly initialized weights

@return model: keras.model.Sequential
"""
def create_cnn():
    #Input shape - image 128x128 pixels in grayscale
    input_shape = (128,128,1) 
    
    model = Sequential()
    model.add(MaxPooling2D((2, 2), input_shape = input_shape))
    model.add(Conv2D(4, (4, 4), kernel_initializer= 'random_normal', bias_initializer='random_normal'))
    model.add(Conv2D(4, (4, 4), kernel_initializer= 'random_normal', bias_initializer='random_normal'))
    model.add(MaxPooling2D((2, 2)))
    model.add(Conv2D(8, (4, 4), kernel_initializer= 'random_normal', bias_initializer='random_normal'))
    model.add(Conv2D(8, (4, 4), kernel_initializer= 'random_normal', bias_initializer='random_normal'))
    model.add(MaxPooling2D((2, 2)))
    model.add(Flatten())
    model.add(Dropout(0.25))
    model.add(Dense(16, activation = relu, kernel_initializer= 'random_normal', bias_initializer='random_normal'))
    model.add(Dense(16, activation = relu, kernel_initializer= 'random_normal', bias_initializer='random_normal'))
    model.add(Dense(3, activation = tanh,  kernel_initializer= 'random_normal', bias_initializer='random_normal'))

    return model


"""
Creates list of CNNs generated by create_cnn().

@param size: int (number of CNNs)

@return cnn_list: list (list of CNNs)
"""
def create_list_cnn(number):
    cnn_list = []
    for i in range(number):
        cnn_list.append(create_cnn())

    return cnn_list


"""
Loads and preprocess image to input shape for CNN created by cnn.py

@param img_path: String (path to image)

@return img: image in desired shape
"""
def preprocess_img_from_path(img_path):
    loaded_img = keras_image.load_img(img_path, color_mode = 'grayscale', target_size=(128, 128))
    array_img = keras_image.img_to_array(loaded_img)
    img = np.expand_dims(array_img, axis=0)

    return img


"""
Functionality testing created while developent
"""
if __name__ == "__main__":
    
    img_name = "nao.jpg"
    img = preprocess_img_from_path(img_name)
    
    c = create_cnn()
    pred = c.predict(img)
    print("Prediction")
    print(pred)

    
    