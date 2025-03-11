import requests
from config import LM_STUDIO_URL
from utils.logging import log_info, log_error
import re

def call_lm_studio(prompt: str) -> str:
    payload = {
        "model": "deepseek-r1-distill-qwen-7b", # we know this sucks, but we need to use it for now
        "messages": [
            {"role": "system", "content": "You are a friendly and helpful AI assistant."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7,
        "max_tokens": -1,  # -1 means no limit (depends on model)
        "stream": False
    }
    try:
        # api post request to lmstudio
        log_info(f"Calling LM Studio API with prompt: {prompt}")
        response = requests.post(LM_STUDIO_URL, json=payload, headers={"Content-Type": "application/json"})
        response.raise_for_status()
        data = response.json()

        # ngl i used chat gpt to generate this parsing stuff
        full_response = data.get("choices", [{}])[0].get("message", {}).get("content", "No response received.")
        think_match = re.search(r"<think>(.*?)</think>", full_response, re.DOTALL)
        reasoning = think_match.group(1).strip() if think_match else "No reasoning provided."
        actual_message = re.sub(r"<think>.*?</think>", "", full_response, flags=re.DOTALL).strip()

        return {"reasoning": reasoning, "reply": actual_message}
    
    except requests.RequestException as e:
        log_error(f"Error calling LM Studio API: {e}")
        return "Error processing your request."