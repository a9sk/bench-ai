import requests
from config import LM_STUDIO_URL

def call_lm_studio(prompt: str) -> str:
    payload = {"prompt": prompt}
    try:
        # api post requst to the lmstudio model 
        response = requests.post(LM_STUDIO_URL, json=payload)
        response.raise_for_status()
        data = response.json()
        return data.get("response", "")
    except requests.RequestException as e:
        # all the logging shall be migrated to utils/logging.py
        print(f"Error calling LM Studio API: {e}")
        return "Error processing your request."
