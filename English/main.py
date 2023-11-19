'''

API inference for English HTR
'''





from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
import numpy as np
import cv2
import uvicorn
from io import BytesIO
from typing import Union
from mltu.inferenceModel import OnnxInferenceModel
from mltu.utils.text_utils import ctc_decoder, get_cer
from mltu.configs import BaseModelConfigs

# Define your ImageToWordModel class here or import from your module
class ImageToWordModel(OnnxInferenceModel):
    def __init__(self, char_list: Union[str, list], *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.char_list = char_list

    def predict(self, image: np.ndarray):
        image = cv2.resize(image, self.input_shape[:2][::-1])
        image_pred = np.expand_dims(image, axis=0).astype(np.float32)
        preds = self.model.run(None, {self.input_name: image_pred})[0]
        text = ctc_decoder(preds, self.char_list)[0]
        return text

# Initialize FastAPI app
app = FastAPI()


# Load model configurations and initialize model
configs = BaseModelConfigs.load("configs.yaml")
model = ImageToWordModel(model_path='model.onnx', char_list=configs.vocab)

# CORS middleware to allow cross-origin requests (for local testing)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    contents = await file.read()
    nparr = np.frombuffer(contents, np.uint8)  # Convert to numpy array
    image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)  # Decode image
    prediction_text = model.predict(image)  # Predict text from image
    return {"prediction": prediction_text}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
