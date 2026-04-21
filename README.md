# Speech to text application

### server.py (FastAPI application)
GCP requirement:
Before running, go to the Google Speech API menu in the GCP console
and enable the API.
If you don't have an API key, get one. 

**Python requirements**:
Application assumes that FastAPI server and Streamlit client are running 
locally. 

Create a Python virtual environment and install modules in requirements.txt.


To run server in terminal (run first):
    uvicorn server:app --port=8080 --reload

### audiorec-streamlit.py (Client)
Streamlit client app that records speech and queries a FastAPI
server app that's driven by Google Speech to extract text content.

To run (in another terminal window):
    streamlit run st-audiorec.py

You must grant microphone access to your browser.
