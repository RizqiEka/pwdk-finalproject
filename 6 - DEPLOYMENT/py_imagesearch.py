import pandas as pd
from py_readdata import readdatarecsys

rdf = readdatarecsys()


def imgsearch(hasil_classifier,area):

    hasil_classifier = str(hasil_classifier)
    hasil = rdf[(rdf['Cuisines'].apply(lambda x: hasil_classifier in x)) & (rdf['City'] == area)]
    hasil.sort_values(['Restaurant Rating'], ascending=False, inplace=True)
    return hasil[0:5][['Restaurant Name', 'Place Type', 'Cuisines', 'Cuisine Regionality','Price for 2','Restaurant Address', 'Restaurant Rating','Restaurant Review','City', 'Province']]

