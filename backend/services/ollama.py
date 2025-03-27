import requests
from config import OLLAMA_URL
from utils.logging import log_info, log_error
import re

def call_ollama(prompt: str) -> dict:
    payload = {
        "model": "deepseek-r1-distill-qwen-7b",  # Model should match the one pulled in Ollama
        "prompt": prompt,
        "stream": False,  # Ollama supports streaming; keep False unless you handle streaming responses
        "temperature": 0.7
    }
    
    try:
        # API request to Ollama
        log_info(f"Calling Ollama API with prompt: {prompt}")
        response = requests.post(f"{OLLAMA_URL}/api/generate", json=payload, headers={"Content-Type": "application/json"})
        response.raise_for_status()
        data = response.json()

        # Ollama's response structure
        full_response = data.get("response", "No response received.")

        # Extract <think> reasoning part (if applicable)
        think_match = re.search(r"<think>(.*?)</think>", full_response, re.DOTALL)
        reasoning = think_match.group(1).strip() if think_match else "No reasoning provided."
        actual_message = re.sub(r"<think>.*?</think>", "", full_response, flags=re.DOTALL).strip()

        return {"reasoning": reasoning, "reply": actual_message}

    except requests.RequestException as e:
        log_error(f"Error calling Ollama API: {e}")
        return {"reasoning": "", "reply": "Error processing your request."}
