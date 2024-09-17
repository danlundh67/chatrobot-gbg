
import os
from dotenv import load_dotenv
import json
import requests


load_dotenv()

EDEN_API_KEY = os.getenv("EDEN_API")


class Bot:
    def __init__(self) -> None:
        self._history = []
    
    def chat(self, prompt):
        headers = {"Authorization": f"Bearer {EDEN_API_KEY}"}

        url = "https://api.edenai.run/v2/text/chat"
        payload = {
            "providers": "openai/gpt-4o-mini",
            "text": prompt,
            "chatbot_global_action": """Du är en lärarassistent som är rolig, du svarar med att skriva svaren i göteborgsdialekt. Du driver och skojar med personer från Stockholm. 
            Du kan hjälpa till med att analysera data.
            Ditt namn är RO BÅT.
    .   """,
            "previous_history": self._history,
            "temperature": 0.5,
            "max_tokens": 500,
        }

        response = requests.post(url, json=payload, headers=headers)
        # print(response.json())
        answer = json.loads(response.text)['openai/gpt-4o-mini']['generated_text']
        
        self._history.append({"role": "user", "message": prompt})
        self._history.append({"role": "assistant", "message": answer})

        return answer

