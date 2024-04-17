# DSC 333: Streamlit client app that records speech and queries a FastAPI
# server app that's driven by Google Speech to extract text content.
# Install streamlit-audiorec first:
#    pip3 install streamlit-audiorec
# To run locally, replace VM_EXTERNAL_IP below with the external IP
# address of your VM (where the FastAPI application is running)
#   streamlit run audiorec-streamlit.py
#
# You must grant microphone access to your browser.

from st_audiorec import st_audiorec
import streamlit as st
import requests

wav_audio_data = st_audiorec()
filename = 'recording.wav'

# Replace with the external IP address of your VM
base_URI = 'http://VM_EXTERNAL_IP:8080/'

if wav_audio_data is not None:
    st.audio(wav_audio_data, format='audio/wav')
    with open(filename, 'wb') as audio_file:
        audio_file.write(wav_audio_data)

    # uploaded_file is the field expected on the FastAPI side
    files = {'uploaded_file': open(filename, 'rb')}

    headers = {'Content-Type': 'multipart-form-data',
            'accept': 'application/json'}

    # Detect text in the recorded audio
    r = requests.post(base_URI + 'speech_to_text/', data=headers, files = files)
    st.subheader('I heard you say:')
    st.write(r.text)
    print(r.text)
