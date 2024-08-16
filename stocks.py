from bs4 import BeautifulSoup
import requests

def scrape_stock_data(symbol):
    url = f"https://finance.yahoo.com/quote/{symbol}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    current_price = soup.find(f"fin-streamer", {"data-symbol":{symbol},"data-field":'regularMarketPrice'})['data-value']
    previous_close = soup.find(f"fin-streamer", {"data-symbol":{symbol},"data-field":'regularMarketPreviousClose'})['data-value']
    print(current_price)


