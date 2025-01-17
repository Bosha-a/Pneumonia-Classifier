import streamlit as st
import pickle as pkl 
from tensorflow import keras
from PIL import Image
import numpy as np 

model = keras.models.load_model('pneumonia.keras')

st.title('X-Ray Pneumonia Classifer')


# File uploader for image input
uploaded_file = st.file_uploader('Upload an X-ray image (PNG, JPG, JPEG)', type=['png', 'jpg', 'jpeg'])

if uploaded_file is not None:

    image = Image.open(uploaded_file).convert('L')  
    image = image.resize((224, 224))  
    image_array = np.array(image) / 255.0 
    image_array = np.expand_dims(image_array, axis=0)  

    if st.button('Predict'):
        prediction = model.predict(image_array)[0][0]
        predicted_class = 'Pneumonia' if prediction > 0.5 else 'Normal'

        if predicted_class == 'Pneumonia':
            st.error(f"Case: {predicted_class}")
        else:
            st.success(f"Case: {predicted_class}")
else:
    st.error("Please upload an image file (PNG, JPG, JPEG).")