"""
    Functions that route the html pages
"""
from flask import render_template, redirect, url_for, request, send_from_directory, flash
from app import app
import os
from werkzeug import secure_filename
from app import predictor 
import csv

def flowerInfo(prediction):
    """
        Inputs: flower species common name
        Outputs: all care and planting info about the inputted flower stored in
        the data.csv file
    """
    with open('../cs121/app/flower-data.csv') as f:
        csv_f = csv.reader(f)
        flowers = {}
        for row in csv_f:
            flowers[row[0]] = row
        return flowers[prediction]

@app.route('/<filename>')
def get_file(filename):
    return send_from_directory('static', filename)

@app.route('/identify', methods=['GET', 'POST'])
def identify():
    """
        Routes/directs server to identify.html page and predicts the flower of 
        an image if the file is uploaded under the right restrictions
    """
    if request.method == 'POST':
        # Check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If user does not select file, browser also
        # submits an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        #If the file is allowed and exists
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            #The file is uploaded to our database
            UPLOAD_FOLDER = '../cs121/static/uploads'
            app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
            save_to = (os.path.join(app.config['UPLOAD_FOLDER'], filename))
            file.save(save_to)
            pred_class, index, output = predictor.model_predict(save_to, '/home/ubuntu/cs121/app')

            # Transforms the tensor into a 1D array
            output_list = [element.item() for element in output.flatten()]

            classes = ['alpineseaholly', 'anthurium', 'artichoke', 'azalea', \
                'ballmoss', 'balloonflower', 'barbetondaisy', 'beardediris', \
                'beebalm', 'birdofparadise', 'bishopofllandaff', \
                'blackberrylily', 'blackeyedsusan', 'blanketflower', \
                'bolerodeepblue', 'bougainvillea', 'bromelia', 'buttercup',\
                'californiapoppy', 'camellia', 'cannalily', 'canterburybells', \
                'capeflower', 'carnation', 'cautleyaspicata', 'clematis', \
                'coltsfoot', 'columbine', 'commondandelion', 'cornpoppy', \
                'cyclamen', 'daffodil', 'desertrose', 'englishmarigold', \
                'firelily', 'foxglove', 'frangipani', 'fritillary', \
                'gardenphlox', 'gaura', 'gazania', 'geranium', \
                'giantwhitearumlily', 'globeflower', 'globethistle', \
                'grapehyacinth', 'greatmasterwort', 'hardleavedpocketorchid',\
                'hibiscus', 'hippeastrum', 'japaneseanemone', 'kingprotea', \
                'lentenrose', 'lotus', 'loveinthemist', 'magnolia', 'mallow', \
                'marigold', 'mexicanaster', 'mexicanpetunia', 'monkshood', \
                'moonorchid', 'morningglory', 'orangedahlia', 'osteospermum', \
                'oxeyedaisy', 'passionflower', 'pelargonium', 'peruvianlily', \
                'petunia', 'pincushionflower', 'pinkprimrose', \
                'pinkyellowdahlia', 'poinsettia', 'primula', \
                'princeofwalesfeathers', 'purpleconeflower', 'redginger', \
                'rose', 'rubylippedcattleya', 'siamtulip', 'silverbush', \
                'snapdragon', 'spearthistle', 'springcrocus', 'stemlessgentian',\
                'sunflower', 'sweetpea', 'sweetwilliam', 'swordlily', \
                'thornapple', 'tigerlily', 'toadlily', 'treemallow','treepoppy',\
                'trumpetcreeper', 'wallflower', 'watercress', \
                'waterlily', 'wildpansy', 'windflower', 'yellowiris']
            # Create list of tuples of the classes and their probabilities, sorted
            flower_prob = list(zip(classes, output_list))
            flower_prob.sort(key=lambda tup: tup[1], reverse = True) 
            top_three = flower_prob[0:3]
            first_prob = round(top_three[0][1], 3)*100
            # If the flower the image is classified to be has low probability, alert user
            if first_prob < 40:
                return render_template('identify.html', alert= True)
            second_prob = round(round(top_three[1][1], 3)*100,4)
            third_prob = round(round(top_three[2][1], 3)*100,4)
            # Get filename of the predicted flower to compare to uploaded flower
            predimg=str(pred_class)+".jpg"
            # Get information about the flower
            flower = flowerInfo(str(pred_class))
            # If no information about the flower, let the user know
            for i in range(len(flower)):
                if str(flower[i]) == "" or str(flower[i]) == " ":
                    flower[i]="Sorry! We don't have extensive information about this flower :("   
            name = flower[1]
            gen_info = flower[2].split('\n')
            lifecycle = flower[3]
            seasons = flower[7]
            difficulty = flower[4]
            planting = flower[5].split('\n')
            sunlight = flower[9].split('\n')
            watering = flower[6].split('\n')
            soil = flower[10].split('\n')
            warnings = flower[8].split('\n')
            website = flower[11]
            citation = flower[12]

            return render_template('displayResult.html', filename=filename, 
                prediciton=pred_class, predictionimg=predimg,
                name=name, top_three = top_three, second_prob = second_prob,
                third_prob = third_prob, gen_info=gen_info, 
                lifecycle = lifecycle, difficulty = difficulty, 
                planting = planting, watering = watering, seasons = seasons, 
                warnings = warnings, sunlight = sunlight, soil = soil, 
                website = website, citation = citation)
    return render_template('identify.html')

#Routes the index page 
@app.route('/')
def home_route():
    return render_template("index.html")

#Routes the about page
@app.route('/about')
def about():
    return render_template('about.html')

#Routes the more information for the database page"
@app.route('/database', methods=['GET', 'POST'])
def database():
    #If more information is requested
    if request.method =='POST':
        species = request.form['flower']
        predimg=species+".jpg"
        flower = flowerInfo(species)
        # Access the information by calling the the specific rows and columns
        # from the .csv file
        for i in range(len(flower)):
            #If the cell in the .csv file is empty
            if str(flower[i]) == "" or str(flower[i]) == " ":
                #Print that we do not have information on the flower
                flower[i]="Sorry! We don't have extensive information about this flower :("
        #If .csv cell does have content, access that row and column
        name = flower[1]
        gen_info = flower[2].split('\n')
        lifecycle = flower[3]
        seasons = flower[7]
        difficulty = flower[4]
        planting = flower[5].split('\n')
        sunlight = flower[9].split('\n')
        watering = flower[6].split('\n')
        soil = flower[10].split('\n')
        warnings = flower[8].split('\n')
        website = flower[11]
        citation = flower[12]
        #Print content of the .csv cells
        return render_template('moreInfo.html',
                predimg=predimg, name=name, gen_info=gen_info, 
                lifecycle = lifecycle, difficulty = difficulty, 
                planting = planting, watering = watering, seasons = seasons, 
                warnings = warnings, sunlight = sunlight, soil = soil, 
                website = website, citation = citation)
    return render_template('database.html')

#Routes the citations page
@app.route('/citations')
def citations():
    return render_template('citations.html')

# Specifies the allowed image types
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
app.config['ALLOWED_EXTENSIONS'] = ALLOWED_EXTENSIONS

# Checks if a file is allowed to be uploaded
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']
