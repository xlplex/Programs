import requests
import time

def send_message(webhook_url, message):
    data = {
        "content": message
    }
    requests.post(webhook_url, json=data)

def main():
    webhook_url = input("Enter your Discord webhook URL: ")

    while True:
        send_message(webhook_url, "Hello, Discord!")
        time.sleep(0.1)  # Send a message every 0.9 seconds

if __name__ == "__main__":
    main()
