'''
API method can be accessed using curl:

curl -X 'POST' \
  'http://VM_EXTERNAL_IP:8080/speech_to_text/' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@AUDIO_FILE.wav;type=audio/wav'

Google sample test code for speech API:
https://github.com/GoogleCloudPlatform/python-docs-samples/blob/main/speech/snippets/transcribe.py

GCP requirement:
Before running, go to the Google Speech API menu in the GCP console
and enable the API

Python requirements (VM side):
Create a Python virtual environment and install modules in requirements.txt:
    pip3 install -r requirements.txt
'''

from fastapi import FastAPI, File, UploadFile
from google.cloud import speech

app = FastAPI()

@app.post('/speech_to_text/')
async def object_detect(uploaded_file: UploadFile):
    path = f"{uploaded_file.filename}"
    response = {}

    content = None
    with open(path, "wb") as out_file:
        content = uploaded_file.file.read()
        out_file.write(content)

    client = speech.SpeechClient()

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
