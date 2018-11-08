import requests
import json

base_url = "https://api.oceanex.pro/v1"

def get_market_list(base_url):
    """ get valid market list """
    method_url = base_url + "/markets"
    r = requests.get(method_url)
    market_data = json.loads(r.text)
    market_list = market_data['data']
    markets = [dic['id'] for dic in market_list]
    print(markets)
    return markets


def get_ticker(base_url, markets=["ocevet"]):
    """get ticker from one market"""
    market = markets[0]
    method_url = base_url + "/tickers/{}".format(str(market))
    r = requests.get(method_url, timeout=5)
    tick_data = json.loads(r.text)
    message = tick_data['message']
    print(message)
    if 'success' not in message.lower():
        quit()
    tick = tick_data['data']['ticker']
    for key, val in tick.items():
        print(key, val)
    return tick

def get_multiple_tickers():
    """get tickers from multiple markets"""
    pass


def get_orderbook(base_url, markets=['ocevet']):
    """get order book"""
    market = markets[0]
    limit = 5
    method_url = base_url + "/order_book"
    data = {
        "market": market,
        "limit": limit
    }
    r = requests.get(method_url, data=data)
    book_data = json.loads(r.text)
    message = book_data['message']
    print(message)
    if 'success' not in message.lower():
        quit()
    book = book_data['data']
    print(book)
    asks = book['asks']
    bids = book['bids']
    print(asks)
    for i in range(len(asks)):
        print(asks[i], bids[i])

### main function ###
get_orderbook(base_url)
