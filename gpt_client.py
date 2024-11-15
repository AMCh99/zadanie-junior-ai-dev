from dotenv import load_dotenv
import os
from openai import OpenAI
import re



load_dotenv()


PRICING = {
    "gpt-4o-2024-08-06": {
        "input_token_cost": 2.50 / 1_000_000,
        "output_token_cost": 10.00 / 1_000_000,
    },
    "gpt-4o-2024-05-13": {
        "input_token_cost": 5.00 / 1_000_000,
        "output_token_cost": 15.00 / 1_000_000,
    },
    "gpt-4o-mini-2024-07-18": {
        "input_token_cost": 0.15 / 1_000_000,
        "output_token_cost": 0.60 / 1_000_000,
    },
    "gpt-4o-mini": {
        "input_token_cost": 0.15 / 1_000_000,
        "output_token_cost": 0.60 / 1_000_000,
    }
}


SYSTEM_CONTENT = (
                "You are a helpful robot that converts txt content to HTML <body> content. "
                "You do not use CSS and JavaScript. Chande encodeing if neede."
                "Use this tags: ['section','div','p','img','figure', 'figcaption']. "
                "Do not use these tags: ['body','html','script','style'] "
                "You can use these tags if needed: ['b','a','span','br','i','h(1-6)']"
                "At the beggining of each section leave <img> tag with attrs src='image_placeholder.jpg' and alt. "
                "The 'alt' attribute for each <img> tag should contain a detailed description that can be used to generate an image with a text-to-image model. "
                "Each <img> tag should be wrapped in a <figure> tag, and the description for the image should be placed inside a <figcaption> tag. "
                )



class GPTClient:
    def __init__(self, api_key=None, model="gpt-4o-mini", temp=0.1, max_tokens=10000):
        self.api_key = api_key or os.getenv('GPT_API_KEY')
        if not self.api_key:
            raise ValueError("API key is required")
        
        self.client = OpenAI(api_key=self.api_key)
        self.model = model
        self.temp = temp
        self.max_tokens = max_tokens
        self.system_content = SYSTEM_CONTENT

    def gpt_response(self, article):
        """Generates a response using OpenAI's GPT model"""
        
        messages = [
                    {"role": "system", "content": self.system_content},
                    {"role": "user", "content": f"Convert the text to HTML <body> content: {article}"}
                    ]
        try:
            response_data = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                max_tokens=self.max_tokens,
                temperature=self.temp,
            )
            
            # Token usage pricing calculation
            usage = response_data.usage
            total_tokens = usage.total_tokens
            prompt_tokens = usage.prompt_tokens
            completion_tokens = usage.completion_tokens
            model_pricing = PRICING.get(self.model, {})
            input_cost = model_pricing.get("input_token_cost", 0) * prompt_tokens
            output_cost = model_pricing.get("output_token_cost", 0) * completion_tokens
            total_cost = input_cost + output_cost
                        
            cleaned_content = re.sub(r'```html|```$', '', response_data.choices[0].message.content, flags=re.DOTALL)
            
            result = {
                "article": cleaned_content.strip(),
                "token_usage": {
                    "total_tokens": total_tokens,
                    "prompt_tokens": prompt_tokens,
                    "completion_tokens": completion_tokens
                    },
                "cost": {
                    "input_cost": input_cost,
                    "output_cost": output_cost,
                    "total_cost": total_cost
                }}
            return result
        except Exception as e:
            print(f"Error occurred: {e}")
            return None


