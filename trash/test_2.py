import cv2
import imutils
from imutils.contours import sort_contours
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

# Load the model
model_path = 'model.h5'  # Replace with the actual path to your .h5 file
model = tf.keras.models.load_model(model_path)

def showImage(img):
    if len(img.shape) == 2:
        plt.imshow(img, cmap='gray')
    else:
        plt.imshow(img)
    plt.show()

def predict_image(path, real=None):
    img = cv2.imread(path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edged = cv2.Canny(blurred, 30, 150)
    cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    cnts = sort_contours(cnts, method="left-to-right")[0]
    chars = []

    for c in cnts:
        (x, y, w, h) = cv2.boundingRect(c)
        roi = gray[y:y + h, x:x + w]
        (tH, tW) = roi.shape

        if tH < tW:
            pad = (tW - tH)
            if pad % 2 != 0:
                roi = cv2.resize(roi, (tW * 2, tH * 2))
                image = cv2.copyMakeBorder(roi, pad, pad, 0, 0, cv2.BORDER_CONSTANT, value=(255, 255, 255))
            else:
                pad = int(pad / 2)
                image = cv2.copyMakeBorder(roi, pad, pad, 0, 0, cv2.BORDER_CONSTANT, value=(255, 255, 255))
        elif tH > tW:
            pad = (tH - tW)
            if pad % 2 != 0:
                roi = cv2.resize(roi, (tW * 2, tH * 2))
                image = cv2.copyMakeBorder(roi, 0, 0, pad, pad, cv2.BORDER_CONSTANT, value=(255, 255, 255))
            else:
                pad = int(pad / 2)
                image = cv2.copyMakeBorder(roi, 0, 0, pad, pad, cv2.BORDER_CONSTANT, value=(255, 255, 255))

        image = cv2.resize(image, (100, 100))
        image = image >= 180
        image = image.astype("int16") * 255
        image = cv2.merge([image, image, image])
        image = image.astype("float32") / 255.0
        image = np.expand_dims(image, axis=-1)
        chars.append((image, (x, y, w, h)))

    boxes = [b[1] for b in chars]
    chars = np.array([c[0] for c in chars], dtype="float32")

    if len(chars) > 0:
        preds = model.predict(chars)
        labelNames = "abcdefghijklmnopqrstuvwxyz"
        sentence = ""

        for (pred, (x, y, w, h)) in zip(preds, boxes):
            i = np.argmax(pred)
            prob = pred[i]
            label = labelNames[i]
            sentence += label
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.putText(img, label, (x - 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 255), 2)

        print(sentence)

        if real:
            print(" ".join(sentence.split()))
            print(" ".join(real.split()))

        showImage(img)

# Predicting image

predict_image("l.jpeg")
