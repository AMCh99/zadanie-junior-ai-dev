from gpt_client import GPTClient

if __name__ == "__main__":
    gpt_client = GPTClient()
    message = "Hello, GPT!"
    response = gpt_client.gpt_response(message)
    if response:
        print(response)