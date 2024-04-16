# Speech to text application

### server.py
GCP requirement:
Before running, go to the Google Speech API menu in the GCP console
and enable the API

**Python requirements (VM side)**:
Create a Python virtual environment and install modules in requirements.txt:
    pip3 install -r requirements.txt

To run (in a terminal on the VM):
  uvicorn server:app --host=0.0.0.0 --port=8080 --reload

### audiorec-streamlit.py (Client)
Streamlit client app that records speech and queries a FastAPI
server app that's driven by Google Speech to extract text content.

To run locally, replace VM_EXTERNAL_IP below with the external IP
address of your VM (where the FastAPI application is running)
   streamlit run audiorec-streamlit.py

You must grant microphone access to your browser.
