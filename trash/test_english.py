import tensorflow as tf
import numpy as np
from keras.preprocessing.image import img_to_array, load_img
from keras.applications.vgg19 import preprocess_input
import os
from PIL import Image

english_characters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'l', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'z', 'y', 'k'
]


def load_model(model_path):
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model file not found: {model_path}")
    return tf.keras.models.load_model(model_path)

def preprocess_image(image_path, target_size=(32, 32)):
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image file not found: {image_path}")
    image = load_img(image_path, color_mode='grayscale', target_size=target_size)
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    image /= 255.0  # Normalize the image
    return image

def predict(model, image):
    prediction = model.predict(image)
    predicted_class = np.argmax(prediction, axis=1)
    return predicted_class

# Define model and image paths
model_path = 'english\english.h5'
image_path = 'english\k.jpeg'

try:
    model = load_model(model_path)
    processed_image = preprocess_image(image_path)
    prediction = predict(model, processed_image)
    print(f"Predicted class: {english_characters[prediction[0]]}")
except Exception as e:
    print(f"An error occurred: {e}")
