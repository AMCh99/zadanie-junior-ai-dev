# Zadanie rekrutacyjne Junior AI Developer OXIDO

## Opis aplikacji

Aplikacja służy do generowania HTML-a z artykułów w formie tekstowej, z wykorzystaniem OpenAI GPT. Proces obejmuje pobranie tekstu z zewnętrznego źródła, przetworzenie go na HTML z odpowiednimi tagami i atrybutami obrazków oraz zapisanie wygenerowanego kodu HTML do pliku.

Aplikacja składa się z kilku plików, które razem tworzą kompletną funkcjonalność:

- **`gpt_client.py`**: Plik odpowiedzialny za komunikację z API OpenAI GPT i generowanie odpowiedzi na podstawie artykułów. Przygotowuje zapytanie, wysyła je do GPT, a następnie przetwarza odpowiedź, generując HTML.
- **`get_text_file.py`**: Plik odpowiedzialny za pobranie tekstu artykułu z zewnętrznego źródła i zapisanie go do pliku lokalnego.
- **`app.py`**: Główny plik uruchamiający aplikację, który integruje wszystkie funkcje: pobiera artykuł, przetwarza go przy pomocy GPT, zapisuje wygenerowany HTML i wyświetla informacje o zużyciu tokenów i kosztach.
- **`template.env`**: Przykładowy plik konfiguracyjny, który należy zmienić na `.env` i wprowadzić swój klucz API.

## Struktura plików

- `gpt_client.py` - zawiera kod do komunikacji z API OpenAI oraz generowanie odpowiedzi.
- `get_text_file.py` - odpowiada za pobieranie tekstu artykułu z URL i zapisanie go w pliku `.txt`.
- `app.py` - główny plik, który wywołuje proces pobierania artykułu, jego przetwarzania i zapisania HTML.
- `.env` - plik konfiguracyjny z Twoim kluczem API do OpenAI.
- `template.env` - szablon pliku `.env`, który należy odpowiednio skonfigurować.
- `podglad.html` - plik wyjściowy, zawierający wygenerowany kod HTML.
- `szablon.html` - szablon HTML, który może zostać użyty do wyświetlania wyników.
- `artykul.html` - plik z wynikiem wygenerowanym przez OpenAI.
- `artykul.txt` - pobrany plik tekstowy.
- `styles.css` - plik CSS, który zawiera style dla wygenerowanego HTML.

## Jak uruchomić aplikację

Aby uruchomić aplikację lokalnie, wykonaj poniższe kroki:

1. **Zmień nazwę pliku `template.env` na `.env`**:
   - W pliku `.env` umieść swój klucz API z OpenAI. Przykład:
     ```
     OPENAI_API_KEY=your-api-key-here
     ```

2. **Zainstaluj wymagane biblioteki**:
   - Użyj poniższego polecenia, aby zainstalować wszystkie wymagane biblioteki z pliku `requirements.txt`:
     ```bash
     pip install -r requirements.txt
     ```

3. **Uruchom aplikację**:
   - Po zainstalowaniu bibliotek, uruchom aplikację używając poniższego polecenia:
     ```bash
     python app.py
     ```

4. **Co się dzieje po uruchomieniu aplikacji**:
   - **Pobranie artykułu**: Aplikacja zaczyna działanie od pobrania artykułu w formie tekstowej z zewnętrznego URL (adres URL jest zdefiniowany w pliku `get_text_file.py`). Tekst jest zapisywany do pliku `artykul.txt` w katalogu roboczym.
   - **Przetworzenie artykułu przez GPT**: Następnie artykuł z pliku `artykul.txt` jest przekazywany do klasy `GPTClient`, która korzysta z API OpenAI GPT do przetworzenia tekstu na kod HTML. Przy generowaniu HTML-a uwzględniane są specjalne tagi HTML oraz atrybuty, w tym m.in. tagi `<img>`, które będą miały odpowiedni opis w `alt` (do wykorzystania z modelami generującymi obrazy na podstawie tekstu).
   - **Zapisanie wygenerowanego HTML**: Po przetworzeniu tekstu przez GPT, wygenerowany HTML jest zapisywany do pliku `artykul.html` w katalogu roboczym.
   - **Zwrócenie informacji o kosztach i tokenach**: Po wygenerowaniu HTML-a aplikacja wyświetli informacje o zużytych tokenach (zarówno wejściowych, jak i wyjściowych) oraz całkowitym koszcie operacji, który jest obliczany na podstawie aktualnych stawek za tokeny w API OpenAI.

5. **Sprawdź wygenerowany HTML**:
   - Po uruchomieniu aplikacji, plik HTML (`artykul.html`) zostanie zapisany w folderze roboczym. Możesz go otworzyć w przeglądarce, aby zobaczyć wynik.

6. **Wyniki**:
   - Aplikacja wygeneruje plik HTML, który będzie zawierał sformatowaną wersję artykułu. Dodatkowo, w konsoli wyświetlone zostaną informacje o zużyciu tokenów oraz całkowitym koszcie operacji.
