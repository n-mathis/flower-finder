from flask import render_template, redirect, url_for, request, send_from_directory, flash
from app import app
import os
from werkzeug import secure_filename
from app import predictor 
import csv

@app.route('/<filename>')
def get_file(filename):
    return send_from_directory('static',filename)

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
            save_to=(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            file.save(save_to)
            pred_class=predictor.model_predict(save_to, '/home/ubuntu/cs121/app')
            return render_template('displayResult.html', filename=filename, prediction=pred_class)
    return render_template('index.html')


@app.route('/more_info', methods=['GET', 'POST'])
def more_info():
    if request.method == 'POST':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('index'))
    preds = request.args.get('preds')

    f = open('Data.csv')
    csv_f = csv.reader(f)
    flowers = {}
    for row in csv_f:
      flowers[row[0]] = row
    return render_template('more.html',prediction=preds)

@app.route('/')
def home_route():
    return flask.render_template("index.html")

@app.route('/database')
def database():
    return render_template('database.html')

@app.route('/citations')
def citations():
    return render_template('citations.html')

# allowed image types
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
app.config['ALLOWED_EXTENSIONS']=ALLOWED_EXTENSIONS

# is file allowed to be uploaded?
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']
