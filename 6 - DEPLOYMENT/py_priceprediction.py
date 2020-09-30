import pickle
import pandas as pd
from sklearn.preprocessing import RobustScaler

model = pickle.load(open("price_pred_zomato.sav",'rb'))
scaler = pickle.load(open("scaler_zomato.sav",'rb'))


def prediction(data):
    scaled = pd.DataFrame(scaler.transform(data), columns=data.columns)
    hasil = model.predict(scaled)
    hasil = int(round(hasil[0]*1000,-2))

    if len(str(hasil)) > 6:
        hasil = "Rp " + str(hasil)[0] + "." + str(hasil)[1:-3] + "." + str(hasil)[-3:]
    else:
        hasil = "Rp " + str(hasil)[:-3] + "." + str(hasil)[-3:]
        
    return hasil
