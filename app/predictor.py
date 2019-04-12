from __future__ import division, print_function
import sys
import os
import glob
import re
from pathlib import Path

# Import fast.ai Library
from fastai import *
from fastai.vision import *

# Flask utils
from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename


#load model
def load_model(model_path):
    path = Path(model_path)
<<<<<<< HEAD
#    classes = 'alpineseaholly', 'anthurium', 'artichoke', 'azalea', 'ballmoss', 'balloonflower', 'barbetondaisy', 'beardediris', 'beebalm', 'birdofparadise', 'bishopofllandaff', 'blackberrylily', 'blackeyedsusan', 'blanketflower', 'bolerodeepblue', 'bougainvillea', 'bromelia', 'buttercup', 'californiapoppy', 'camellia', 'cannalily', 'canterburybells', 'capeflower', 'carnation', 'cautleyaspicata', 'clematis', 'coltsfoot', 'columbine', 'commondandelion', 'cornpoppy', 'cyclamen', 'daffodil', 'desertrose', 'englishmarigold', 'firelily', 'foxglove', 'frangipani', 'fritillary', 'gardenphlox', 'gaura', 'gazania', 'geranium', 'giantwhitearumlily', 'globeflower', 'globethistle', 'grapehyacinth', 'greatmasterwort', 'hardleavedpocketorchid', 'hibiscus', 'hippeastrum', 'japaneseanemone', 'kingprotea', 'lentenrose', 'lotus', 'loveinthemist', 'magnolia', 'mallow', 'marigold', 'mexicanaster', 'mexicanpetunia', 'monkshood', 'moonorchid', 'morningglory', 'orangedahlia', 'osteospermum', 'oxeyedaisy', 'passionflower', 'pelargonium', 'peruvianlily', 'petunia', 'pincushionflower', 'pinkprimrose', 'pinkyellowdahlia', 'poinsettia', 'primula', 'princeofwalesfeathers', 'purpleconeflower', 'redginger', 'rose', 'rubylippedcattleya', 'siamtulip', 'silverbush', 'snapdragon', 'spearthistle', 'springcrocus', 'stemlessgentian', 'sunflower', 'sweetpea', 'sweetwilliam', 'swordlily', 'thornapple', 'tigerlily', 'toadlily', 'treemallow', 'treepoppy', 'trumpetcreeper', 'wallflower', 'watercress', 'waterlily', 'wildpansy', 'windflower', 'yellowiris']
     classes = ['cat', 'lion','toy']

 data2 = ImageDataBunch.single_from_classes(path, classes, ds_tfms=get_transforms(), size=224).normalize(imagenet_stats)
=======
    classes = ['cat', 'lion','toy']
    data2 = ImageDataBunch.single_from_classes(path, classes, ds_tfms=get_transforms(), size=224).normalize(imagenet_stats)
>>>>>>> 3a5340879a75b29b0127371dfdc54cacef98bf2e
    learn = create_cnn(data2, models.resnet34)
    learn.load('stage-2')
    return learn

def model_predict(img_path, model_path):
    """
       model_predict will return the preprocessed image
    """
    learn = load_model(model_path)
    img = open_image(img_path)
    pred_class,pred_idx,outputs = learn.predict(img)
    return pred_class
