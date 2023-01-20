import json
import requests

# API endpoint
api_endpoint = "https://api.openai.com/v1/engines/davinci/completions"


# API key
api_key = "YOUR_API_KEY_GOES_KERE"

# Input prompt
prompt = "What's the weather like today?"

# API parameters
# Update parameters as necessary for your program
params = {
    "prompt": prompt,
    "max_tokens": 128,
    "stop": "."
}

# API headers
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

# Send API request
response = requests.post(api_endpoint, json=params, headers=headers)

# Print response
print(response.text)
