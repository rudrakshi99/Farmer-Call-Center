import pickle


# Would need to add the model file
def crop_classifier():
    crop_recommendation_model_path = 'models/RandomForest.pkl'
    crop_recommendation_model = pickle.load(
        open(crop_recommendation_model_path, 'rb'))
    return crop_recommendation_model