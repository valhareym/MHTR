import cv2
import typing
import numpy as np

from mltu.inferenceModel import OnnxInferenceModel
from mltu.utils.text_utils import ctc_decoder, get_cer

class ImageToWordModel(OnnxInferenceModel):
    def __init__(self, char_list: typing.Union[str, list], *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.char_list = char_list

    def predict(self, image: np.ndarray):
        image = cv2.resize(image, self.input_shape[:2][::-1])

        image_pred = np.expand_dims(image, axis=0).astype(np.float32)

        preds = self.model.run(None, {self.input_name: image_pred})[0]

        text = ctc_decoder(preds, self.char_list)[0]

        return text

if __name__ == "__main__":
    import pandas as pd
    from tqdm import tqdm
    from mltu.configs import BaseModelConfigs

    configs = BaseModelConfigs.load("English\configs.yaml")

    model = ImageToWordModel(model_path='English\model.onnx', char_list=configs.vocab)

   
    image_path = "English/3.png"
    image = cv2.imread(image_path)

    prediction_text = model.predict(image)

    print(f"Image: {image_path}, Label:, Prediction: {prediction_text}")

        
        # resize by 4x
    image = cv2.resize(image, (image.shape[1] * 4, image.shape[0] * 4))
    cv2.imshow("Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
