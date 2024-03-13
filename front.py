import streamlit as st
import requests
import time

# CSS styles
st.markdown("""
<style>
    /* App background color */
    body {
        background-color: #35374B;
    }

    /* Sidebar styling */
    .css-1d391kg {
        background-color: #35374B;
        padding: 10px;
    }


    /* Button styling */
    .stButton>button {
        border: 2px solid #4CAF50;
        border-radius: 20px;
        color: white;
        background-color: #4CAF50;
        padding: 10px 24px;
        cursor: pointer;
        font-size: 18px;
    }

</style>
""", unsafe_allow_html=True)

# The HTML and CSS code for the button
github_repo_url = "https://github.com/ignaciogomenuka"
github_logo_base64 = "https://i.pinimg.com/564x/95/7c/4d/957c4dd9aa815cc1de2040cc1259589f.jpg"
button_html = f"""
<a href="{github_repo_url}" target="_blank" style="text-decoration: none;">
    <div style="
        margin: 1rem auto;
        padding: 0.5rem 1rem;
        background-color: #f6f8fa;
        border: 1px solid rgba(27,31,35,.15);
        border-radius: .5rem;
        box-shadow: rgba(27,31,35,.04) 0 1px 0 inset;
        display: flex;
        align-items: center;
        justify-content: center;
        cursor: pointer;
        color: #24292e;
        font-size: 1rem;
        font-weight: 500;">
        <img src="{github_logo_base64}" alt="GitHub Logo" style="height: 20px; margin-right: 0.5rem;"/>
        Go to Repo
    </div>
</a>
"""

# Sidebar navigation
st.sidebar.image('https://info.lewagon.com/hubfs/Mexico/Logo_Red%26White-1.png', width=200)
st.sidebar.title('Navigation')
page = st.sidebar.radio('Go to', ['Introduction', 'Upload & Analysis', 'About us'])
st.sidebar.markdown(button_html, unsafe_allow_html=True)

# Introduction page content
if page == 'Introduction':
    st.title('Handball Goal Detection App')
    st.subheader('Welcome!')
    st.write("""
        This app uses advanced computer vision to track handball matches and detect goal plays.
        Simply upload a video of a match, and the app will analyze it to return clips where goals are detected.
        Navigate to the 'Upload & Analysis' page to get started!
    """)

elif page == 'Upload & Analysis':
    st.title('Obtener tiempos de partidos')
    url = "http://127.0.0.1:8000/predict_video"
    uploaded_file = st.file_uploader("Upload a .mp4 file:", type="mp4")

    if st.button('Obtener predicciones'):
        if uploaded_file is not None:
            # Add a placeholder for the progress bar and message
            progress_bar = st.progress(0)
            progress_message = st.empty()

            # Dummy loop to simulate progress
            for i in range(100):
                # Update the progress bar
                progress_bar.progress(i + 1)

                # Update progress message
                progress_message.text(f'Processing... {i+1}%')

                # Sleep to simulate processing time
                time.sleep(0.05)

            # Once the loop is done, make the API call
            files = {'file': uploaded_file.getvalue()}
            response = requests.post(url, files=files)
            progress_message.text('Finishing up...')

            if response.ok:
                predictions = response.json()
                progress_message.text('Analysis complete!')
                st.write(predictions)
            else:
                st.error("Error en la respuesta de la API.")
            # Reset the progress bar and message
            progress_bar.empty()
            progress_message.empty()

elif page == 'About us':

    from PIL import Image
    image = st.image('https://info.lewagon.com/hubfs/Mexico/Logo_Red%26White-1.png', width=200)
    st.title('About us')

    col1, col2, col3 = st.columns(3)

    with col1:
        st.image('https://avatars.githubusercontent.com/u/103946112?v=4', width=200)  # Replace with the path to your image
        st.markdown("""
                     ## Ignacio Muñoz Gomeñuka

                      description
                    """)

    with col2:
        st.image('https://avatars.githubusercontent.com/u/68247059?v=4', width=200)  # Replace with the path to your image
        st.markdown("""
                     ## Felipe Alvarez Diaz

                      description
                    """)
    with col3:
        st.image('https://avatars.githubusercontent.com/u/100483669?v=4', width=200)  # Replace with the path to your image
        st.markdown("""
                     ## Gustavo Oliviero

                      description
                    """)
