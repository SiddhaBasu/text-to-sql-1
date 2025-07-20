import requests

def call_gemini(prompt, endpoint_url, api_key):
    """
    Call the Gemini AI endpoint with the prompt.
    """
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {
            "maxOutputTokens": 1024,
            "temperature": 0.2,
            "stopSequences": ["\n\n"]
        }
    }
    response = requests.post(endpoint_url, headers=headers, json=payload)
    response.raise_for_status()
    # Gemini's response format may differ; adjust as needed
    return response.json()["candidates"][0]["content"]["parts"][0]["text"] 