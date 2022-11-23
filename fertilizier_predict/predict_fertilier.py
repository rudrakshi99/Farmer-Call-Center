import pickle

def recommend_fertilizer(data):
    model_path = 'models/fertilizer.pkl'
    model = pickle.load(open(model_path, 'rb'))
    return model.predict(data)