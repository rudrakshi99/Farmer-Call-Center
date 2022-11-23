import pickle


def recommend_crop(data):
    crop_recommendation_model_path = 'models/RandomForest.pkl'
    crop_recommendation_model = pickle.load(
        open(crop_recommendation_model_path, 'rb'))
    return crop_recommendation_model.predict(data)