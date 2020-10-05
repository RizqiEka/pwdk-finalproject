from flask import Flask, render_template, request
import pandas as pd
from py_readdata import readdata, readdatarecsys
from py_priceprediction import prediction
from py_recommendersystem import getrecommendationall
from py_imageclassifier import imgclassify
from py_imagesearch import imgsearch
from werkzeug.utils import secure_filename
import os
from flask.helpers import flash

app=Flask(__name__)

UPLOAD_FOLDER = r'D:\Personal Data\Data Science\Personal Project\Final Project Purwadhika - JKT Foodies One Stop Guide\6 - DEPLOYMENT\static\images'
ALLOWED_EXTENSION = set(['png', 'jpeg', 'jpg', 'gif'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSION

@app.route('/')
def home():
    return render_template ('home.html')

@app.route('/data')
def data():
    data = readdata()
    return render_template ('data.html', data=data)

@app.route('/plots')
def plots():
    data = readdata()
    return render_template('plots.html', data=data)


@app.route('/classify', methods=['GET', 'POST'])
def classify():
    if request.method == 'POST':
        file = request.files['file']

        if 'file' not in request.files:
            flash('No file part')
            return render_template('imageclassify.html')
        
        if file.filename == '':
            flash('No selected file')
            return render_template('imageclassify.html')
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            global hasil_classifier
            hasil_classifier = imgclassify(filepath)
            return render_template('resultclassifier.html', data=hasil_classifier)
    return render_template('imageclassify.html')


@app.route('/imgsearch', methods=['GET', 'POST'])
def imagesearch():
    if request.method == 'POST':
        data = request.form
        area = str(data['area'])
        cuisine = hasil_classifier
        hasil_imgsearch = imgsearch(hasil_classifier,area)
        return render_template('resultimgsearch.html', data = hasil_imgsearch)
    return render_template('resultclassifier.html')



@app.route('/recomenderall',methods= ['GET','POST'])
def recommendall():
    if request.method == 'POST':
        data = request.form
        name = data['name']
        rec_plc = int(data['rec_plc'])
        rec_csne = int(data['rec_csne'])
        rec_rgn = int(data['rec_rgn'])
        rec_city = int(data['rec_city'])
        rec_price = int(data['rec_price'])

        hasil_recommend_all = getrecommendationall(name, rec_plc, rec_csne, rec_rgn, rec_city, rec_price)

        if type(hasil_recommend_all) != pd.DataFrame:
            return render_template('resultfailrecom.html')
        else:
            return render_template('resultrecomall.html', data=hasil_recommend_all)
    return render_template('recommend-all.html')


@app.route('/prediction',methods= ['GET','POST'])
def prediction_html():
    if request.method == 'POST':
        data = request.form

        rsvm = int(data['reservasimejarekom'])
        fd = int(data['finedining'])
        cd = int(data['casualdining'])
        mm = int(data['makanmewah'])
        alc = int(data['alkoholtersedia'])
        wifi = int(data['wifitersedia'])
        rpt = int(data['ruangprivate'])
        wnb = int(data['hanyawinedanbir'])
        rate = float(data['rating'])
        rev = float(data['review'])
        pvlt = int(data['parkirvalettersedia'])
        cock = int(data['cocktailtersedia'])
        bft = int(data['buffettersedia'])
        brt = int(data['barat'])
        bir = int(data['hanyabir'])
        ent = int(data['liveent'])
        nl = int(data['nightlife'])
        tw = int(data['takeawaytersedia'])
        qb = int(data['quickbites'])
        sm = int(data['ruangmerokok'])
        bar = int(data['bar'])
        ind = int(data['indonesia'])
        tmin = int(data['tokominuman'])

        feature = pd.DataFrame({
            'reservasimejadirekomendasikan' : [rsvm],
            'Fine Dining' : [fd],
            'Casual Dining' : [cd],
            'makanmewah' : [mm],
            'alkoholtersedia' : [alc],
            'wifitersedia' : [wifi],
            'ruangpribaditersedia' : [rpt],
            'hanyawinedanbir' : [wnb],
            'Restaurant Rating' : [rate],
            'Restaurant Review' : [rev],
            'parkirvalettersedia' : [pvlt],
            'menyediakancocktail' : [cock],
            'buffet' : [bft],
            'Barat' : [brt],
            'hanyabir' : [bir],
            'liveentertainment' : [ent],
            'kehidupanmalam' : [nl],
            'bawapulangtersedia' : [tw],
            'Quick Bites' : [qb],
            'areamerokok' : [sm],
            'Bar' : [bar],
            'Indonesia' : [ind],
            'Toko Minuman' : [tmin]
        })

        hasil_pred = prediction(fd, feature)
        return render_template('resultprediction.html', hasil_prediksi=hasil_pred)
    return render_template('prediction.html')



if __name__ == '__main__':
    app.run(debug=True,port=2000)


