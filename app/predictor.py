"""
    All functions that use fast.ai and relate to the model
"""
from __future__ import division, print_function
# import sys
# import os
# import glob
# import re
from pathlib import Path

# Import fast.ai Library
from fastai import *
from fastai.vision import *

# Flask utils
# from flask import Flask, redirect, url_for, request, render_template
# from werkzeug.utils import secure_filename


#load model
def load_model(model_path):
    """
    Input: model path to create databunch and a learner with the given model
    """
    path = Path(model_path)
    classes = ['alpineseaholly', 'anthurium', 'artichoke', 'azalea', 'ballmoss',\
        'balloonflower', 'barbetondaisy', 'beardediris', 'beebalm', \
        'birdofparadise', 'bishopofllandaff', 'blackberrylily', \
        'blackeyedsusan', 'blanketflower', 'bolerodeepblue', 'bougainvillea', \
        'bromelia', 'buttercup', 'californiapoppy', 'camellia', 'cannalily', \
        'canterburybells', 'capeflower', 'carnation', 'cautleyaspicata', \
        'clematis', 'coltsfoot', 'columbine', 'commondandelion', 'cornpoppy',\
        'cyclamen', 'daffodil', 'desertrose', 'englishmarigold', 'firelily',\
        'foxglove', 'frangipani', 'fritillary', 'gardenphlox', 'gaura', 'gazania',\
        'geranium', 'giantwhitearumlily', 'globeflower', 'globethistle', \
        'grapehyacinth','greatmasterwort', 'hardleavedpocketorchid', 'hibiscus',\
        'hippeastrum','japaneseanemone', 'kingprotea', 'lentenrose', 'lotus', \
        'loveinthemist', 'magnolia', 'mallow', 'marigold', 'mexicanaster',\
        'mexicanpetunia', 'monkshood', 'moonorchid', 'morningglory', \
        'orangedahlia', 'osteospermum', 'oxeyedaisy', 'passionflower',\
        'pelargonium', 'peruvianlily', 'petunia', 'pincushionflower', \
        'pinkprimrose','pinkyellowdahlia', 'poinsettia', 'primula', \
        'princeofwalesfeathers', 'purpleconeflower', 'redginger', 'rose',\
        'rubylippedcattleya', 'siamtulip', 'silverbush', 'snapdragon', \
        'spearthistle', 'springcrocus', 'stemlessgentian', 'sunflower',\
        'sweetpea','sweetwilliam', 'swordlily', 'thornapple', 'tigerlily', \
        'toadlily', 'treemallow', 'treepoppy', 'trumpetcreeper', 'wallflower',\
        'watercress', 'waterlily', 'wildpansy','windflower', 'yellowiris']

    #Create databunch and convolutional neural network
    data2 = ImageDataBunch.single_from_classes(path, classes, ds_tfms=get_transforms(), \
    size=224).normalize(imagenet_stats)
    learn = create_cnn(data2, models.resnet34)
    # Load the model we trained
    learn.load('first-stage')
    #Return the model
    return learn

#load the image of the predicted flower
def model_predict(img_path, model_path):
    """
    model_predict will return the preprocessed image
    """
    learn = load_model(model_path)
    img = open_image(img_path)
    pred_class, pred_idx, outputs = learn.predict(img)
    return pred_class, pred_idx, outputs
