from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image
import io
from fastapi.middleware.cors import CORSMiddleware
# Define FastAPI app
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Load the TensorFlow model
model = load_model('arabic.hdf5')

# Arabic characters for mapping the prediction
arabic_chars = [
    '', 'ا', 'ب', 'ت', 'ث', 'خ', 'ح', 'ج', 'د', 'ذ', 'ن', 'ز', 'س', 'ش', 'ص', 'ض', 'ط', 'ظ', 'ع', 'غ', 'ف', 'ق', 'ك', 'ل', 'م', 'ر', 'ه', 'و', 'ي'
]

# Pydantic model for response
class Prediction(BaseModel):
    label: int
    character: str

def preprocess_image(image_file):
    # Read the image from in-memory bytes
    image = Image.open(io.BytesIO(image_file))
    image = image.convert('L')  # Convert to grayscale
    image = image.resize((32, 32))
    image = np.array(image)
    image = image.reshape(1, 32, 32, 1)  # Add batch dimension
    image = image.astype('float32') / 255.0  # Normalize
    return image

@app.post("/predict/", response_model=Prediction)
async def predict(file: UploadFile = File(...)):
    image_data = await file.read()
    img = preprocess_image(image_data)
    pred = model.predict(img)
    predicted_label = int(np.argmax(pred))  # Convert to native Python int
    predicted_char = arabic_chars[predicted_label]
    return {"label": predicted_label, "character": predicted_char}

# Run the app
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
