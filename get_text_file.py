import requests

URL = "https://cdn.oxido.pl/hr/Zadanie%20dla%20JJunior%20AI%20Developera%20-%20tresc%20artykulu.txt"
SAVE_PATH="artykul.txt"

def get_text_file():
    """Downloads the text from given url and saves it to a txt file"""
    try:
        response = requests.get(URL)
        if response.status_code == 200:
            with open(SAVE_PATH, 'w', encoding='utf-8') as file:
                file.write(response.text)
            print(f"File saved to {SAVE_PATH}")
            return response.text
        else:
            print(f"Download error: {response.status_code}")
    except Exception as e:
        print(f"Error: {e}")
