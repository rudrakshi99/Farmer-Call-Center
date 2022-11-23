import pickle

def min_max(data):
    model_path = 'models/minmax.pkl'
    model = pickle.load(open(model_path, 'rb'))
    return model.transform(data)