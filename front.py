import streamlit as st
import requests

st.header('Obtener tiempos de partidos')
url = "http://127.0.0.1:8000/predict_video"
uploaded_file = st.file_uploader("Upload a .mp4 file:", type="mp4")

if st.button('Obtener predicciones'):
    if uploaded_file is not None:
        files = {'file': uploaded_file.getvalue()}
        response = requests.post(url, files=files)

        if response.ok:
            predictions = response.json()
            st.write(predictions)
        else:
            st.error("Error en la respuesta de la API.")
