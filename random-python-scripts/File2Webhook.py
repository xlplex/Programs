import tkinter as tk
from tkinter import filedialog
import requests

def send_file_to_discord_webhook():
    webhook_url = webhook_entry.get()
    if webhook_url:
        try:
            with open(file_path, 'rb') as file:
                payload = {
                    "file": file
                }
                requests.post(webhook_url, files=payload)
                print("File sent successfully to Discord webhook!")
        except Exception as e:
            print(f"An error occurred: {e}")
    else:
        print("Webhook URL not provided")

def browse_file():
    global file_path
    file_path = filedialog.askopenfilename()

def save_webhook():
    webhook_url = webhook_entry.get()
    if webhook_url:
        with open("webhook.txt", "w") as file:
            file.write(webhook_url)
            print("Webhook URL saved to 'webhook.txt'")
    else:
        print("Please enter a webhook URL")

root = tk.Tk()
root.title("File Drop to Discord Webhook")

root.geometry("200x125")

file_path = ""

# Load saved webhook URL if exists
try:
    with open("webhook.txt", "r") as file:
        saved_webhook = file.read()
except FileNotFoundError:
    saved_webhook = ""

webhook_label = tk.Label(root, text="Discord Webhook URL:")
webhook_label.pack()

webhook_entry = tk.Entry(root)
webhook_entry.pack()
webhook_entry.insert(0, saved_webhook)

browse_button = tk.Button(root, text="Browse", command=browse_file)
browse_button.pack()

send_button = tk.Button(root, text="Send File to Webhook", command=send_file_to_discord_webhook)
send_button.pack()

save_button = tk.Button(root, text="Save Webhook URL", command=save_webhook)
save_button.pack()

root.mainloop()
