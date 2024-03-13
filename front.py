import streamlit as st
import requests
import os


# Establece la variable de entorno antes de cualquier otra lógica que la utilice
os.environ['DEEPSORT_CONFIG_PATH'] = '/home/felipe-alvarez/code/Fast_final/yolov8/ultralytics/yolo/v8/segment/deep_sort_pytorch/configs/deep_sort.yaml'

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
