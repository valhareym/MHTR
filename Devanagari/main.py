from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array, load_img
from io import BytesIO
from PIL import Image

app = FastAPI()
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

devanagari_chars = [
    'ऀ', 'ँ', 'ं', 'ः',
    'ऄ', 'अ', 'आ', 'इ', 'ई', 'उ', 'ध', 'ऋ','न', 'ऌ', 'ऍ', 'ऎ', 'ए', 'ऐ', 'ऑ', 'ऒ', 'ओ', 'औ', 
    'क', 'ख', 'ग', 'घ', 'ङ', 'च', 'छ', 'ज', 'झ', 'ञ', 'ट', 'ठ', 'ड', 'ढ', 'ण', 'त', 'थ', 'द', 'ऊ', 'ऩ', 'प', 'फ', 'ब', 'भ', 'म', 'य', 'र', 'ऱ', 'ल', 'ळ', 'ऴ', 'व', 'श', 'ष', 'स', 'ह', 
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
# Load your model
model = load_model('devangiri.h5')

@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    contents = await file.read()
    image = Image.open(BytesIO(contents)).convert("L")
    image = image.resize((28, 28))
    image_array = img_to_array(image)
    image_array = image_array.reshape(1, 28, 28, 1)
    image_array = image_array / 255.0

    predictions = model.predict(image_array)
    pin = np.argmax(predictions)
    # Replace 'devanagari_chars' with your actual array of characters
    character = devanagari_chars[pin]
    
    return JSONResponse(content={"character": character})


