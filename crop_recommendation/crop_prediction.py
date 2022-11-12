import numpy as np
from crop_model import crop_classifier
from weather import weather_fetch


def make_crop_recommendation(N,P,K,ph,rainfall, city):
    if weather_fetch(city) != None:
        temperature, humidity = weather_fetch(city)
        data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
        my_prediction = crop_classifier.predict(data)
        return my_prediction[0]
    else:
        return 0