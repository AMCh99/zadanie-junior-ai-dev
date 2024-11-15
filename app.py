from gpt_client import GPTClient
from get_text_file import get_text_file
import sys

sys.stdout.reconfigure(encoding='utf-8') # to prevent UnicodeEncodeError

def main():
    gpt_client = GPTClient()
    message = "Hello, GPT!"
    response = gpt_client.gpt_response(message)
    if response:
        print(response)
    text_file = get_text_file()
    print(text_file)

if __name__ == "__main__":
    main()