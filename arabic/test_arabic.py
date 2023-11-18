import tensorflow as tf
from tensorflow.keras.models import load_model
import cv2
import numpy as np

arabic_chars = [
  '',  'ا', 'ب', 'ت', 'ث', 'خ', 'ح', 'ج','د', 'ذ','ن', 'ز', 'س', 'ش', 'ص', 'ض', 'ط', 'ظ', 'ع', 'غ', 'ف', 'ق', 'ك', 'ل', 'م','ر', 'ه', 'و', 'ي'
]


model = load_model('arabic.hdf5')
def preprocess_image(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (32, 32))
    img = img.reshape(1, 32, 32, 1)  # Add batch dimension
    img = img.astype('float32') / 255.0  # Normalize pixel values
    return img
def predict_image(image_path, model):
    img = preprocess_image(image_path)
    pred = model.predict(img)
    predicted_label = np.argmax(pred)
    return predicted_label


image_path = 'arabic/arabic2.jpg'
prediction = predict_image(image_path, model)
print(prediction)
print("Predicted label:", arabic_chars[prediction])
