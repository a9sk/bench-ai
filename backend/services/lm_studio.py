import requests
from config import LM_STUDIO_URL
from utils.logging import log_info, log_error

def call_lm_studio(prompt: str) -> str:
    payload = {"prompt": prompt}
    try:
        # api post request to lmstudio
        log_info(f"Calling LM Studio API with prompt: {prompt}")
        response = requests.post(LM_STUDIO_URL, json=payload)
        response.raise_for_status()
        data = response.json()
        return data.get("response", "")
    except requests.RequestException as e:
        log_error(f"Error calling LM Studio API: {e}")
        return "Error processing your request."
