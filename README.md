# Wstęp

## Tworzenie zapytań HTML, format JSON i zapytania w Pythonie

### Tworzenie zapytań HTML

Zapytania HTML to sposób na przesyłanie danych z przeglądarki internetowej do serwera. Składają się z trzech części:

* **Metoda:** Określa typ żądania, np. GET (pobranie danych), POST (wysłanie danych), PUT (zaktualizowanie danych) lub
  DELETE (usunięcie danych).
* **Adres URL:** Określa miejsce docelowe żądania, czyli adres URL serwera.
* **Nagłówki:** Zawierają dodatkowe informacje o żądaniu, np. typ danych (Content-Type) lub autoryzację (Authorization).
* **Treść:** Opcjonalnie zawiera dane przesyłane do serwera, zwykle w formacie formularza lub JSON.

Przykład zapytania HTML GET:

```html
GET /data.json HTTP/1.1
Host: example.com
Content-Type: application/json
Authorization: Bearer my-token

{"id": 123, "name": "John Doe"}
```

### Format JSON

JSON (JavaScript Object Notation) to format wymiany danych oparty na tekstowych kluczach i wartościach. Jest powszechnie
używany do przesyłania danych między aplikacjami internetowymi.

Przykład obiektu JSON:

```json
{
  "id": 123,
  "name": "John Doe",
  "email": "johndoe@example.com"
}
```

Przykład użycia

```python
import json

# Przykładowe dane JSON
json_string = '{"name": "John", "age": 30, "city": "New York"}'

# Używamy json.loads() do przekształcenia danych JSON na słownik Pythona
data = json.loads(json_string)

print(data)  # Wyświetli: {'name': 'John', 'age': 30, 'city': 'New York'}
print(data['name'])  # Wyświetli: John

# Teraz przekształcimy słownik Pythona z powrotem na dane JSON za pomocą json.dumps()
json_data = json.dumps(data)

print(json_data)  # Wyświetli: {"name": "John", "age": 30, "city": "New York"}
```

W powyższym przykładzie, najpierw przekształcamy łańcuch znaków JSON na słownik Pythona za pomocą json.loads().
Następnie, przekształcamy ten słownik z powrotem na łańcuch znaków JSON za pomocą json.dumps(). Pamiętaj, że
json.dumps() zwraca łańcuch znaków reprezentujący dane JSON, a nie prawdziwe dane JSON. Jeśli chcesz zapisać te dane do
pliku, musisz otworzyć plik w trybie tekstowym i zapisać łańcuch znaków do pliku.

### Tworzenie zapytań w Pythonie

W Pythonie można używać biblioteki `requests` do tworzenia zapytań HTTP. Oto przykład, jak wysłać zapytanie GET i pobrać
dane JSON:

```python
import requests

url = "https://example.com/data.json"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("Błąd:", response.status_code)
```

Ten kod wysyła zapytanie GET do adresu URL `https://example.com/data.json`. Jeśli żądanie zakończy się powodzeniem (kod
statusu 200), dane JSON zostaną zdekodowane i wydrukowane. W przeciwnym razie zostanie wyświetlony komunikat o błędzie.

Można również użyć biblioteki `requests` do wysyłania innych typów żądań, takich jak POST, PUT i DELETE. Można również
przesyłać dane w formacie JSON do serwera.

# Zadanie

Uzupełnij impelmentacje klas `StockDataAnalyzer`(`stock_data_analyzer.py`) oraz `CompanyInfoFetcher`(`company_info_fetcher.py`) korzystając z API `polygon.io` w celu pobrania
danych o spółkach giełdowych.

### Użyj endpointów API udestępnionych przez `polygon.io`:
- [Tickers](https://polygon.io/docs/stocks/get_v3_reference_ticker)
- [Ticker Details](https://polygon.io/docs/stocks/get_v3_reference_tickers__ticker)

### Klucz API:
Koniecznie zastęp klucz w pliku `keys.py` kluczem API wygenerowanym na stronie `polygon.io`.
Api ma ograniczoną liczbę zapytań, wieć czasem konieczne będzie odczekanie kilku minut przed kolejnym zapytaniem.

### Testy
W sumie można zdobyć 100 punktów.
- `PYTHONPATH=$PYTHONPATH:`pwd` python -m unittest do_not_modify/test_mocked_stock_data_analyzer.py -k test_calculate_average_price` - 7 pkt.
- `PYTHONPATH=$PYTHONPATH:`pwd` python -m unittest do_not_modify/test_real_stock_data_analyzer.py -k test_calculate_average_price` - 7 pkt.
- `PYTHONPATH=$PYTHONPATH:`pwd` python -m unittest do_not_modify/test_mocked_stock_data_analyzer.py -k test_calculate_max_price` - 7 pkt.
- `PYTHONPATH=$PYTHONPATH:`pwd` python -m unittest do_not_modify/test_real_stock_data_analyzer.py -k test_calculate_max_price` - 7 pkt.
- `PYTHONPATH=$PYTHONPATH:`pwd` python -m unittest do_not_modify/test_real_stock_data_analyzer.py -k test_calculate_min_price` - 7 pkt.
- `PYTHONPATH=$PYTHONPATH:`pwd` python -m unittest do_not_modify/test_mocked_stock_data_analyzer.py -k test_calculate_min_price` - 7 pkt.
- `PYTHONPATH=$PYTHONPATH:`pwd` python -m unittest do_not_modify/test_mocked_stock_data_analyzer.py -k test_calculate_volume` - 7 pkt.
- `PYTHONPATH=$PYTHONPATH:`pwd` python -m unittest do_not_modify/test_real_stock_data_analyzer.py -k test_calculate_volume` - 7 pkt.
- `PYTHONPATH=$PYTHONPATH:`pwd` python -m unittest do_not_modify/test_mocked_stock_data_analyzer.py -k test_calculate_price_change` - 7 pkt.
- `PYTHONPATH=$PYTHONPATH:`pwd` python -m unittest do_not_modify/test_real_stock_data_analyzer.py -k test_calculate_price_change` - 7 pkt.
- `PYTHONPATH=$PYTHONPATH:`pwd` python -m unittest do_not_modify/test_mocked_stock_data_analyzer.py -k test_calculate_price_change_percentage` - 7 pkt.
- `PYTHONPATH=$PYTHONPATH:`pwd` python -m unittest do_not_modify/test_real_stock_data_analyzer.py -k test_calculate_price_change_percentage` - 7 pkt.

- `PYTHONPATH=$PYTHONPATH:`pwd` python -m unittest do_not_modify/test_mocked_company_info_fetcher.py` - 8 pkt.
- `PYTHONPATH=$PYTHONPATH:`pwd` python -m unittest do_not_modify/test_real_company_info_fetcher.py` - 8 pkt.


