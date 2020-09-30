import pickle
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from py_readdata import readdatarecsys

cv_csn = pickle.load(open("recom_cuisine.sav",'rb'))
cv_rgn = pickle.load(open("recom_cuisine_region.sav",'rb'))
cv_rest = pickle.load(open("recom_place.sav",'rb'))

cos_sin_csne=cosine_similarity(cv_csn)
cos_sin_rgn=cosine_similarity(cv_rgn)
cos_sin_rest=cosine_similarity(cv_rest)
cos_sin_cat=(cos_sin_csne*0.4)+(cos_sin_rgn*0.3)+(cos_sin_rest*0.3)

rdf = readdatarecsys()

def getrecommendationall(name):

    idx=rdf[rdf['Restaurant Name']==name].index[0]
    rest_similar=pd.Series(cos_sin_cat[idx])
    idx_similar=rest_similar.sort_values(ascending=False).head(6).index
    recommend=rdf.loc[idx_similar]
    recommend.reset_index(drop=True,inplace=True)
    hasil = recommend[1:6][['Restaurant Name', 'Place Type', 'Cuisines', 'Cuisine Regionality','Price for 2','Restaurant Address', 'Restaurant Rating','Restaurant Review','City', 'Province']]

    return hasil 
