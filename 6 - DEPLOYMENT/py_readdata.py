import pandas as pd

def readdata():
    df = pd.read_csv('RDF - WebReady.csv', encoding='latin1')
    return df

def readdatarecsys():
    df = pd.read_csv('RDF - Recommender System.csv', encoding='latin1')
    return df

