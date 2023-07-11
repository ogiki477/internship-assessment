import requests
from dotenv import load_dotenv
import os 
from os import sys

url = 'https://sunbird-ai-api-5bq6okiwgq-ew.a.run.app'

load_dotenv()

def translate_text(source_language, target_language, text, token):

    token = os.getenv('token')
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    payload = {
        "source_language": source_language,
        "target_language": target_language,
        "text": text
    }

    response = requests.post(f"{url}/tasks/translate", headers=headers, json=payload)

    if response.status_code == 200:
        translated_text = response.json()["text"]
        return translated_text
    else:
        return f"Translation Error: {response.status_code}, {response.text}"

def get_language_choice(message, choices):
    while True:
        choice = input(message)
        if choice in choices:
            return choice
        elif choice == 'quit':
            sys.exit(0)
        else:
            print("Invalid choice. Please try again.")

def main():
    

   
        auth_type = input("Choose authentication type (token or login-credentials): ")

        if auth_type == 'token':
            token = input('Enter your authentication token: ')
        else:
            username = input('Enter your username: ')
            password = input('Enter your password: ')
            creds = {
                'username': username,
                'password': password
            }
            response = requests.post(f'{url}/auth/token', data=creds)
            token = response.json()['access_token']

        source_language = get_language_choice("Please choose the source language: ",
                                                ["English", "Luganda", "Runyankole", "Ateso", "Lugbara", "Acholi"])

        if source_language == "English":
            target_language = get_language_choice("Please choose the target language (one of Luganda, Runyankole, Ateso, Lugbara, or Acholi): ",
                   
                   
                                                    ["Luganda", "Runyankole", "Ateso", "Lugbara", "Acholi"])
        
        else:
            target_language = "English"
            

        text = input("Enter the text to translate: ")

        translated_text = translate_text(source_language, target_language, text, token)

        print("Translated text:", translated_text)
        
        translated_text = translate_text(target_language,source_language, text, token)

        print("Translated text From English Back to the source Language:", translated_text)
        

if __name__ == "__main__":

    main()


