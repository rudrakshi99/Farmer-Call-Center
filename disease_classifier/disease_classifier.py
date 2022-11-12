from disease_identifier_model import disease_classifier_model

from disease_classifier.predict_image import predict_image

# Use image file here
img = ''
disease_model = disease_classifier_model()
prediction = predict_image(img, model=disease_model)