from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()

class GPTClient:
    def __init__(self, api_key=None, model="gpt-4o-mini", temp=0.1, max_tokens=10000):
        self.api_key = api_key or os.getenv('GPT_API_KEY')
        if not self.api_key:
            raise ValueError("API key is required")
        
        self.client = OpenAI(api_key=self.api_key)
        self.model = model
        self.temp = temp
        self.max_tokens = max_tokens

    def gpt_response(self, message):
        """Generates a response using OpenAI's GPT model"""
        try:
            response_data = self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": message}],
                max_tokens=self.max_tokens,
                temperature=self.temp
            )
            return response_data
        except Exception as e:
            print(f"Error occurred: {e}")
            return None


