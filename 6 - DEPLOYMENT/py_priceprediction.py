import pickle
import pandas as pd
from sklearn.preprocessing import RobustScaler

modelA = pickle.load(open("price_pred_zomato_fulldata.sav",'rb'))
scalerA = pickle.load(open("scaler_zomato_fulldata.sav",'rb'))
modelB = pickle.load(open("price_pred_zomato_nooutlierprice.sav",'rb'))
scalerB = pickle.load(open("scaler_zomato_nooutlierprice.sav",'rb'))

def prediction(finedining, feature):
    if finedining == 1:
        feature = feature[['reservasimejadirekomendasikan', 'Fine Dining', 'Casual Dining', 'makanmewah', 'alkoholtersedia', 'wifitersedia', 'ruangpribaditersedia', 'hanyawinedanbir', 'Restaurant Rating', 'Restaurant Review', 'parkirvalettersedia', 'menyediakancocktail', 'buffet', 'Barat', 'hanyabir', 'liveentertainment', 'kehidupanmalam', 'bawapulangtersedia', 'Quick Bites']]
        scaled = pd.DataFrame(scalerA.transform(feature), columns=feature.columns)
        hasil = modelA.predict(scaled)
        hasil = int(round(hasil[0]*1000,-2))
    else:
        feature = feature[['Casual Dining', 'reservasimejadirekomendasikan', 'wifitersedia', 'alkoholtersedia', 'hanyabir', 'Barat', 'Restaurant Review', 'ruangpribaditersedia', 'areamerokok', 'Restaurant Rating', 'Bar', 'kehidupanmalam', 'hanyawinedanbir', 'parkirvalettersedia', 'menyediakancocktail', 'liveentertainment', 'Toko Minuman', 'Indonesia', 'Quick Bites']]
        scaled = pd.DataFrame(scalerB.transform(feature), columns=feature.columns)
        hasil = modelB.predict(scaled)
        hasil = int(round(hasil[0]*1000,-2))

    if len(str(hasil)) > 6:
        hasil = "Rp " + str(hasil)[0] + "." + str(hasil)[1:-3] + "." + str(hasil)[-3:]
    else:
        hasil = "Rp " + str(hasil)[:-3] + "." + str(hasil)[-3:]
        
    return hasil
