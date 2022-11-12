
import io
from tkinter import Image

import disease_identifier_model
import torch
from PIL import Image
from torchvision import transforms


def predict_image(img, model):
    """
    Transforms image to tensor and predicts disease label
    :params: image
    :return: prediction (string)
    """
    transform = transforms.Compose([
        transforms.Resize(256),
        transforms.ToTensor(),
    ])
    image = Image.open(io.BytesIO(img))
    img_t = transform(image)
    img_u = torch.unsqueeze(img_t, 0)

    # Get predictions from model
    yb = model(img_u)
    # Pick index with highest probability
    _, preds = torch.max(yb, dim=1)
    prediction = disease_identifier_model.disease_classes[preds[0].item()]
    # Retrieve the class label
    return prediction