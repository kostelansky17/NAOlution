from keras import backend as K
from keras.models import Sequential
from keras.layers.convolutional import Conv2D
from keras.layers.convolutional import MaxPooling2D
from keras.layers.core import Dense, Flatten, Dropout
from keras.activations import relu, tanh
from keras.preprocessing import image
from keras.initializers import random_normal
import numpy as np
import tensorflow as tf

def create_cnn():
    input_shape = (128,128,1)
    model = Sequential()
    
    model.add(Conv2D(8, (4, 4), kernel_initializer= 'random_normal', bias_initializer='random_normal', input_shape = input_shape))
    model.add(Conv2D(16, (4, 4), kernel_initializer= 'random_normal', bias_initializer='random_normal'))
    model.add(Conv2D(32, (4, 4), kernel_initializer= 'random_normal', bias_initializer='random_normal'))
    model.add(MaxPooling2D((4, 4)))
    model.add(Flatten())
    model.add(Dropout(0.25))
    model.add(Dense(16, activation = relu, kernel_initializer= 'random_normal', bias_initializer='random_normal'))
    model.add(Dense(16, activation = relu, kernel_initializer= 'random_normal', bias_initializer='random_normal'))
    model.add(Dense(3, activation = tanh,  kernel_initializer= 'random_normal', bias_initializer='random_normal'))

    return model

def create_list_of_cnn(size):
    cnn_list = []
    for i in range(size):
        cnn_list.append(create_cnn())

    return cnn_list

def preprocess_img(img_path):
    img = image.load_img(img_path, color_mode = 'grayscale', target_size=(128, 128))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)

    return x

if __name__ == "__main__":
    
    img_name = "nao.jpg"
    img = preprocess_img(img_name)
    
    cnns = create_list_of_cnn(5)

    for c in cnns:
        pred = c.predict(img)
        print("Prediction")
        print(pred)

    
    