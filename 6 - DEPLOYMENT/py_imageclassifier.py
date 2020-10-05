import pickle
import pandas as pd
import numpy as np
from tensorflow import keras
from tensorflow.keras.preprocessing import image


def imgclassify(files):

    model = keras.models.load_model('ZomateTF09.h5')
    category = {0: 'Ayam', 1: 'Bakmi', 2: 'Bakso', 3: 'Desserts', 4: 'Kopi', 5: 'Kue & Roti', 6: 'Seafood', 7: 'Snacks', 8: 'Soto', 9: 'Tea'}

    img = image.load_img(files, target_size=(160, 160))
    img_tensor = image.img_to_array(img)                    
    img_tensor = np.expand_dims(img_tensor, axis=0)        
    img_tensor /= 255. 

    prediction = model.predict(img_tensor)
    pred_class_indices = np.argmax(prediction, axis=1)
    img_category = [category[a] for a in pred_class_indices]
    img_result = img_category[0]

    return img_result 
