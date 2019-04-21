"""
    functions that route the html pages
"""
from flask import render_template, redirect, url_for, request, send_from_directory, flash
from app import app
import os
from werkzeug import secure_filename
from app import predictor 
import csv

def flowerInfo(prediction):
    with open('../cs121/app/Data.csv') as f:
        csv_f = csv.reader(f)
        flowers = {}
        for row in csv_f:
            flowers[row[0]] = row
        return flowers[prediction]

@app.route('/<filename>')
def get_file(filename):
    return send_from_directory('static', filename)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            save_to = (os.path.join(app.config['UPLOAD_FOLDER'], filename))
            file.save(save_to)
            pred_class, index, output = predictor.model_predict(save_to, '/home/ubuntu/cs121/app')
            flower = flowerInfo(str(pred_class))
            name = flower[1]


            flower_prob = []

            output = output.toList()

            classes = ['alpineseaholly', 'anthurium', 'artichoke', 'azalea', 'ballmoss', 'balloonflower', \
        'barbetondaisy', 'beardediris', 'beebalm', 'birdofparadise', 'bishopofllandaff', \
        'blackberrylily', 'blackeyedsusan', 'blanketflower', 'bolerodeepblue', 'bougainvillea', \
        'bromelia', 'buttercup', 'californiapoppy', 'camellia', 'cannalily', 'canterburybells', \
        'capeflower', 'carnation', 'cautleyaspicata', 'clematis', 'coltsfoot', 'columbine', \
        'commondandelion', 'cornpoppy', 'cyclamen', 'daffodil', 'desertrose', 'englishmarigold', \
        'firelily', 'foxglove', 'frangipani', 'fritillary', 'gardenphlox', 'gaura', 'gazania', \
        'geranium', 'giantwhitearumlily', 'globeflower', 'globethistle', 'grapehyacinth', \
        'greatmasterwort', 'hardleavedpocketorchid', 'hibiscus', 'hippeastrum', \
        'japaneseanemone', 'kingprotea', 'lentenrose', 'lotus', 'loveinthemist', 'magnolia', \
        'mallow', 'marigold', 'mexicanaster', 'mexicanpetunia', 'monkshood', 'moonorchid', \
        'morningglory', 'orangedahlia', 'osteospermum', 'oxeyedaisy', 'passionflower',\
        'pelargonium', 'peruvianlily', 'petunia', 'pincushionflower', 'pinkprimrose', \
        'pinkyellowdahlia', 'poinsettia', 'primula', 'princeofwalesfeathers', 'purpleconeflower', \
        'redginger', 'rose', 'rubylippedcattleya', 'siamtulip', 'silverbush', 'snapdragon', \
        'spearthistle', 'springcrocus', 'stemlessgentian', 'sunflower', 'sweetpea', \
        'sweetwilliam', 'swordlily', 'thornapple', 'tigerlily', 'toadlily', 'treemallow', \
        'treepoppy', 'trumpetcreeper', 'wallflower', 'watercress', 'waterlily', 'wildpansy', \
        'windflower', 'yellowiris']

        #for i in len(classes)
            #flower_prob.append(
             #   {"flower": classes[i], "prob": output[i]})
        #flower_prob = sorted(predictions, key=lambda x: x["output"], reverse=True)
        #flower_prob = predictions[0:5]
        


            return render_template('displayResult.html', filename=filename, prediction=pred_class,
             name=name, index = index, output = output)
    return render_template('index.html')

@app.route('/more_info', methods=['GET', 'POST'])
def more_info():
    if request.method == 'POST':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('index'))
    preds  = request.args.get('preds')
    index  = request.args.get('index')
    output  = request.args.get('output')
    flower = flowerInfo(preds)
    name = flower[1]
    gen_info = flower[2]
    lifecycle = flower[3]
    seasons = flower[7]
    difficulty = flower[4]
    planting = flower[5]
    sunlight = flower[9]
    watering = flower[6]
    soil = flower[10]
    warnings = flower[8]
    website = flower[11]
    citation = flower[12]

    return render_template('more.html', prediction = name, flower = flower, name = name, \
        gen_info=gen_info, lifecycle = lifecycle, difficulty = difficulty, planting = planting, \
        watering = watering, seasons = seasons, warnings = warnings, sunlight = sunlight, \
        soil = soil, website = website, citation = citation)

@app.route('/')
def home_route():
    return flask.render_template("index.html")

@app.route('/database')
def database():
    return render_template('database.html')

@app.route('/citations')
def citations():
    return render_template('citations.html')

@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('index'))
    # show the form, it wasn't submitted
    return render_template('index.html')

# allowed image types
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
app.config['ALLOWED_EXTENSIONS'] = ALLOWED_EXTENSIONS

# is file allowed to be uploaded?
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']