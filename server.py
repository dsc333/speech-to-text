'''
GCP requirement:
Go to the Google Speech API menu in the GCP console and enable it.
If you don't already have an API key, get one.  

Python environment setup:
Create a Python virtual environment and install modules in requirements.txt.
Include your API key in .env.  

Google sample test code for speech API:
https://github.com/GoogleCloudPlatform/python-docs-samples/blob/main/speech/snippets/transcribe.py
'''

from fastapi import FastAPI, File, UploadFile
from google.cloud import speech
from dotenv import load_dotenv
import os

load_dotenv()

# Read API KEY
API_KEY=os.environ.get('API_KEY')

if not API_KEY:
    print('No API key found.')

app = FastAPI()

@app.post('/speech_to_text/')
async def object_detect(uploaded_file: UploadFile):
    path = f"{uploaded_file.filename}"
    response = {}

    content = None
    with open(path, "wb") as out_file:
        content = uploaded_file.file.read()
        out_file.write(content)

    client = speech.SpeechClient(client_options={"api_key": API_KEY})

    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        language_code="en-US",
        audio_channel_count=2,
    )

    response = client.recognize(config=config, audio=audio)

    # Each result is for a consecutive portion of the audio. Iterate through
    # them to get the transcripts for the entire audio file.
    for result in response.results:
        response = result.alternatives[0].transcript
        # The first alternative is the most likely one for this portion.
        print(f"Transcript: {response}")

    return response
