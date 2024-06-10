import requests
from datetime import datetime, timedelta

class StockDataAnalyzer:
    """
    Inicjalizuje obiekt klasy StockDataAnalyzer.

    :param api_key: Klucz API do serwisu Polygon.io.
    :param ticker: Symbol giełdowy firmy, której dane chcemy analizować.
    :param start_date: Data rozpoczęcia analizy w formacie 'YYYY-MM-DD'.
    :param end_date: Data zakończenia analizy w formacie 'YYYY-MM-DD'.
    """
    def __init__(self, api_key, ticker, start_date, end_date):
        pass


    """
    Oblicza i zwraca średnią cenę akcji dla określonego okresu.
    Średnia cena akcji to suma cen otwarcia i zamknięcia podzielona przez 2.

    :return: Średnia cena akcji dla określonego okresu.
    """
    def calculate_average_price(self):
        pass

    """
    Zwraca najwyższą cenę akcji dla określonego okresu.
    Najwyższa cena akcji to najwyższa cena, do której doszło podczas sesji giełdowej.

    :return: Najwyższa cena akcji dla określonego okresu.
    """
    def calculate_max_price(self):
        pass

    """
    Zwraca najniższą cenę akcji dla określonego okresu.
    Najniższa cena akcji to najniższa cena, do której doszło podczas sesji giełdowej.

    :return: Najniższa cena akcji dla określonego okresu.
    """
    def calculate_min_price(self):
        pass

    """
    Oblicza i zwraca całkowity wolumen akcji dla określonego okresu.
    Wolumen akcji to liczba akcji, które zmieniły właściciela w danym okresie.

    :return: Całkowity wolumen akcji dla określonego okresu.
    """
    def calculate_volume(self):
        pass

    """
    Oblicza i zwraca zmianę ceny od początku do końca okresu.
    Zmiana ceny to różnica między ceną otwarcia na początku okresu a ceną zamknięcia na końcu okresu.

    :return: Zmiana ceny od początku do końca okresu.
    """
    def calculate_price_change(self):
        pass

    """
    Oblicza i zwraca procentową zmianę ceny od początku do końca okresu.
    Procentowa zmiana ceny to zmiana ceny wyrażona jako procent ceny otwarcia.

    :return: Procentowa zmiana ceny od początku do końca okresu.
    """
    def calculate_price_change_percentage(self):
        pass