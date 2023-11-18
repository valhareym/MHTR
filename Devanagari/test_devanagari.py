from numpy import argmax
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array, load_img

# Load the trained model
model = load_model('Devanagari/devangiri.h5')
devanagari_chars = [
    'ऀ', 'ँ', 'ं', 'ः',
    'ऄ', 'अ', 'आ', 'इ', 'ई', 'उ', 'ऊ', 'ऋ','न', 'ऌ', 'ऍ', 'ऎ', 'ए', 'ऐ', 'ऑ', 'ऒ', 'ओ', 'औ', 
    'क', 'ख', 'ग', 'घ', 'ङ', 'च', 'छ', 'ज', 'झ', 'ञ', 'ट', 'ठ', 'ड', 'ढ', 'ण', 'त', 'थ', 'द', 'ध', 'ऩ', 'प', 'फ', 'ब', 'भ', 'म', 'य', 'र', 'ऱ', 'ल', 'ळ', 'ऴ', 'व', 'श', 'ष', 'स', 'ह', 
    'ऺ','४', '०', '१', '२', '३', '५', '६', '७', '८', '९',
    'ई', '००',
    'ई', 'ऽ', 
    'ा', 'ि', 'ी', 'ु', 'ू', 'ृ', 'ॄ', 'ॅ', 'ॆ', 'े', 'ै', 'ॉ', 'ॊ', 'ो', 'ौ', '्', 
    'ॎ', 'ॏ', 
    'ॐ', 
    '॑', '॒', 
    '॓', '॔', 
    'ॕ', 
    'ॖ', 'ॗ', 
    'क़', 'ख़', 'ग़', 'ज़', 'ड़', 'ढ़', 'फ़', 'य़', 
    'ॠ', 'ॡ', 'ॢ', 'ॣ', 
    '।', '॥', 
    '०', '१', '२', '३', '४', '५', '६', '७', '८', '९', 
    '॰', 'ॱ', 
    'ॲ', 
    'ॳ', 'ॴ', 'ॵ', 
    'ॶ', 'ॷ', 
    'ॸ', 'ॹ', 'ॺ', 
    'ॻ', 'ॼ', 'ॽ', 'ॾ', 'ॿ'
]

# Define the image preprocessing function
def preprocess_image(image_path):
    # Load the image with the target size of 28x28 and in grayscale
    img = load_img(image_path, color_mode="grayscale", target_size=(28, 28))
    
    # Convert the image to an array
    img = img_to_array(img)
    
    # Reshape the array for the model (adding batch dimension)
    img = img.reshape(1, 28, 28, 1)
    
    # Rescale the pixel values to [0, 1]
    img = img / 255.0

    return img

# Example usage
# Replace 'path/to/your/image.jpg' with the actual path to your image
image_path = 'Devanagari/NA.jpg'
preprocessed_image = preprocess_image(image_path)

# Predict using the model
predictions = model.predict(preprocessed_image)
pin = argmax(predictions)
print(devanagari_chars[pin])
