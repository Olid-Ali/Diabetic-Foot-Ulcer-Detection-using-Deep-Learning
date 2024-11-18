import base64
import cv2
import pandas as pd
import streamlit as st
from keras.models import load_model
import numpy as np


def set_background(image_file):
    """
    This function sets the background of a Streamlit app to an image specified by the given image file.

    Parameters:
        image_file (str): The path to the image file to be used as the background.

    Returns:
        None
    """
    with open(image_file, "rb") as f:
        img_data = f.read()
    b64_encoded = base64.b64encode(img_data).decode()
    style = f"""
        <style>
        .stApp {{
            background-image: url(data:image/png;base64,{b64_encoded});
            background-size: cover;
        }}
        </style>
    """
    st.markdown(style, unsafe_allow_html=True)


def predictor(img):
    img_size = (224, 224)

    scale = 1
    try:
        s = int(scale)
        s2 = 1
        s1 = 0
    except:
        split = scale.split('-')
        s1 = float(split[1])
        s2 = float(split[0].split('*')[1])

    img = np.array(img)

    # Resize and preprocess the image
    img = cv2.resize(img, img_size)
    img = img * s2 - s1
    img = np.expand_dims(img, axis=0)

    # Make prediction using the loaded model
    model = load_model('./model/EfficientNetB3_ulcer_classify.04.h5')
    p = np.squeeze(model.predict(img))
    index = np.argmax(p)
    index = int(index)
    probability = p[index]

    return probability, index
