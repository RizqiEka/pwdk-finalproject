import pickle
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from py_readdata import readdatarecsys

cv_csn = pickle.load(open("recom_cuisine.sav",'rb'))
cv_rgn = pickle.load(open("recom_cuisine_region.sav",'rb'))
cv_plc = pickle.load(open("recom_place.sav",'rb'))
cv_city = pickle.load(open("recom_city.sav", "rb"))

cosin_csne=cosine_similarity(cv_csn)
cosin_rgn=cosine_similarity(cv_rgn)
cosin_plc=cosine_similarity(cv_plc)
cosin_city=cosine_similarity(cv_city)

rdf = readdatarecsys()

def getrecommendationall(name, rec_plc, rec_csne, rec_rgn, rec_city, rec_price):

    try:
        idx=rdf[rdf['Restaurant Name']==name].index[0]

        if rec_plc + rec_csne + rec_rgn + rec_city + rec_price == 0:
            hasil = 0
            pass

        elif rec_price == 0:
            cosin_all = ((cosin_csne*rec_csne) + (cosin_rgn*rec_rgn) + (cosin_plc*rec_plc) + (cosin_city*rec_city)) / (rec_csne + rec_rgn + rec_plc + rec_city)
    
        else:
            prc_arr = np.load("recom_price.npy", allow_pickle=True)
            cosin_all = ((cosin_csne*rec_csne) + (cosin_rgn*rec_rgn) + (cosin_plc*rec_plc) + (cosin_city*rec_city) + (prc_arr*rec_price)) / (rec_csne + rec_rgn + rec_plc + rec_city + rec_price)

        rest_similar=pd.Series(cosin_all[idx])
        idx_similar=rest_similar.sort_values(ascending=False).head(6).index
        recommend=rdf.loc[idx_similar]
        recommend.reset_index(drop=True,inplace=True)
        hasil = recommend[1:6][['Restaurant Name', 'Place Type', 'Cuisines', 'Cuisine Regionality','Price for 2','Restaurant Address', 'Restaurant Rating','Restaurant Review','City', 'Province']]

    except:

        hasil = 0

    return hasil 
