import requests

def call_llama3(prompt, endpoint_url, api_key):
    """
    Call the Llama 3 70B endpoint with the prompt.
    """
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "prompt": prompt,
        "max_tokens": 1024,
        "temperature": 0.2,
        "stop": ["\n\n"]
    }
    response = requests.post(endpoint_url, headers=headers, json=payload)
    response.raise_for_status()
    return response.json()["choices"][0]["text"] 