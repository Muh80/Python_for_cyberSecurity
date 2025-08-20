from dotenv import load_dotenv
import os
from requests import Session, Response

load_dotenv()

api_key = os.getenv("COIN_MARKET_API_SECRET")

GET_PRICE_URL = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/map'

parameters = {
  'symbol': 'BTC'
}

headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': api_key,
}

session = Session()
session.headers.update(headers)

try:
    response = session.get(url=GET_PRICE_URL, params=parameters)
    data = response.json()
    print(data)

except Exception as e:
    print(e)
    
