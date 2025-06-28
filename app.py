import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Load model
@st.cache_resource
def load_covid_model():
    return load_model('covid_classifier.h5')

model = load_covid_model()

# Class labels
class_labels = ['COVID', 'NORMAL', 'PNEUMONIA']

# App title
st.title("COVID-19 Chest X-ray Classifier")
st.markdown("Upload a chest X-ray image to predict COVID-19, Normal, or Pneumonia.")

# File uploader
uploaded_file = st.file_uploader("Upload a Chest X-ray Image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    img = Image.open(uploaded_file).convert("RGB")
    st.image(img, caption='Uploaded Image', use_container_width=True)

    # Preprocess the image
    img_resized = img.resize((224, 224))
    img_array = image.img_to_array(img_resized) / 255.0
    img_batch = np.expand_dims(img_array, axis=0)

    if st.button("Classify"):
        prediction = model.predict(img_batch)
        predicted_class = class_labels[np.argmax(prediction)]

        st.success(f"Predicted Class: **{predicted_class}**")
        st.bar_chart(prediction[0])
        st.write("Prediction Probabilities:")
        for i, label in enumerate(class_labels):
            st.write(f"{label}: {prediction[0][i]:.2f}")