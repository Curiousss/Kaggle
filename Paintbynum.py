# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 20:33:46 2017

@author: Meera
"""
#import numpy as np
import pandas as pd
from skimage.transform import resize
from keras.preprocessing.image import load_img, img_to_array
#from keras.backend import tf as ktf
DATA_PATH = "C:\\Users\\Meers\\Documents\\Techie\\kaggle\\data\\"
TRAIN_DIR = "train_1\\"

def get_image(filename):

    image = load_img(DATA_PATH+TRAIN_DIR+filename)
    imagedata = img_to_array(image)
    #print(imagedata.shape)
    imagedata = imagedata/255
    imagefin = resize(imagedata, (28,28,3))
    #print(imagefin.shape)
    return imagefin


def get_train_images():
    paintings = pd.read_csv("data/train_info1.csv")
    # Vincent Van Gogh
    Van_Gogh_paintings = paintings[(paintings["artist"] ==
                                             "10bc951c2eb4a2f05fa773bdaace4e3b")]
    Other_paintings = paintings[(paintings["artist"] !=
                                             "10bc951c2eb4a2f05fa773bdaace4e3b")]
    '''
    train_images = []
    for filename in abstract_paintings["filename"]:
        train_images.append(get_image(filename))
    '''
    train_images = [get_image(filename) for filename in Van_Gogh_paintings["filename"]]
    other_images = [get_image(filename) for filename in Other_paintings["filename"]]
    return train_images, other_images

def get_pairs(pair1, pair2):
    x = []
    y = []
    return x , y
train_images, other_images = get_train_images()
#get_image("10.jpg")
