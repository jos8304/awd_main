from bs4 import BeautifulSoup
import requests

def scrape_stock_data(symbol):
    url = f"https://finance.yahoo.com/quote/{symbol}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            current_price = soup.find(f"fin-streamer", {"data-symbol":{symbol},"data-field":'regularMarketPrice'})['data-value']
            price_changed = soup.find(f"fin-streamer", {"data-symbol":{symbol},"data-field":'regularMarketChange'})['data-value']
            persentage_changed = soup.find(f"fin-streamer", {"data-symbol":{symbol},"data-field":'regularMarketChangePercent'})['data-value']
            previous_close = soup.find(f"fin-streamer", {"data-symbol":{symbol},"data-field":'regularMarketPreviousClose'})['data-value']
            week_52_range = soup.find(f"fin-streamer", {"data-symbol":{symbol},"data-field":'fiftyTwoWeekRange'})['data-value']
            week_52_high,week_52_low = week_52_range.split('-')
            # week_52_high = soup.find(f"fin-streamer", {"data-symbol":{symbol},"data-field":'fiftyTwoWeekRange'})['data-value']
            # week_52_low = soup.find(f"fin-streamer", {"data-symbol":{symbol},"data-field":'regularMarketPreviousClose'})['data-value']
            market_cap = soup.find(f"fin-streamer", {"data-symbol":{symbol},"data-field":'marketCap'})['data-value']
            pe_ratio = soup.find(f"fin-streamer", {"data-symbol":{symbol},"data-field":'trailingPE'})['data-value']
            dividend_yield = soup.find(f"span", {"class":'value yf-tx3nkj'}).text
            
            
            stock_response = {
                'current_price' : current_price,
                'previous_close': previous_close,
                'price_changed': price_changed,
                'persentage_changed': persentage_changed,
                'week_52_high':week_52_high,
                'week_52_low':week_52_low,
                'market_cap':market_cap,
                'pe_ratio':pe_ratio,
                'dividend_yield':dividend_yield,

            }
            return stock_response
        else:
            return f'Error {symbol}'
    
    except Exception as e:
        # print(f"Error is {e}")
        return None


