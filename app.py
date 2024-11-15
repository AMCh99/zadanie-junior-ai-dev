from gpt_client import GPTClient
from get_text_file import get_text_file


def save_html(html_content, output_file='artykul.html'):
    try:
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(html_content)
        print(f"HTML content successfully saved to {output_file}")
    except Exception as e:
        print(f"Error while saving HTML content: {e}")

def main():
    gpt_client = GPTClient()
    text_file = get_text_file()

    response = gpt_client.gpt_response(text_file)
    if response:
        save_html(response["article"])
        print(response["token_usage"], response["cost"])
        


if __name__ == "__main__":
    main()