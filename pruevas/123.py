# Importing necessary libraries
import tkinter as tk
from tkinter import scrolledtext
import requests

class WitAIChat:
    def __init__(self, root):
        self.root = root
        self.root.title('Chat with Wit.ai')

        self.messages = scrolledtext.ScrolledText(self.root, state='disabled', width=50, height=20, bg='white', fg='black')
        self.messages.grid(row=0, column=0, padx=10, pady=10)

        self.entry = tk.Entry(self.root, width=40)
        self.entry.grid(row=1, column=0, padx=10, pady=10)
        self.entry.bind('<Return>', self.send_message)

        self.send_button = tk.Button(self.root, text='Send', command=self.send_message)
        self.send_button.grid(row=1, column=1, padx=10, pady=10)

        self.WIT_AI_TOKEN = '5RW5APRAWCEW6B5545H2IQY2FH4MMGXA'

    def send_message(self, event=None):
        message = self.entry.get()
        if message.strip() == '':
            return

        self.messages.config(state='normal')
        self.messages.insert(tk.END, f'User: {message}\n')
        self.messages.config(state='disabled')

        # Clear the entry box
        self.entry.delete(0, tk.END)

        # Get response from Wit.ai
        self.get_wit_response(message)

    def get_wit_response(self, message):
        url = f'https://api.wit.ai/message?v=20210320&q={message}'
        headers = {'Authorization': f'Bearer {self.WIT_AI_TOKEN}'}

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            wit_response = response.json()
            self.display_response(wit_response)
        except requests.exceptions.RequestException as e:
            self.display_response({'error': str(e)})

    def display_response(self, response):
        self.messages.config(state='normal')
        if 'error' in response:
            self.messages.insert(tk.END, f'Bot: Error fetching response from Wit.ai.\n')
        else:
            self.messages.insert(tk.END, f'Bot: {response}\n')

            intent_name = response['intents'][0]['name']
            # message_subject_value = response['entities']['wit$message_subject:message_subject'][0]['value']

            if intent_name == "create_user":
                self.messages.insert(tk.END, f'Bot: Se ha creado el usuario  \n')
                print(response)

    
        self.messages.config(state='disabled')

if __name__ == '__main__':
    root = tk.Tk()
    chat_app = WitAIChat(root)
    root.mainloop()