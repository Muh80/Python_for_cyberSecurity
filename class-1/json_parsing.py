import json


raw_json = """
{"results":[
  {"id":1,"domain":"example.com","tags":["malware","c2"]},
  {"id":2,"domain":"safe-site.org","tags":[]}
]}
"""

crypto = {'status': {'timestamp': '2025-08-19T10:36:03.916Z', 'error_code': 0, 'error_message': None, 'elapsed': 23, 'credit_count': 1, 'notice': None}, 'data': [{'id': 1, 'rank': 1, 'name': 'Bitcoin', 'symbol': 'BTC', 'slug': 'bitcoin', 'is_active': 1, 'status': 1, 'first_historical_data': '2010-07-13T00:05:00.000Z', 'last_historical_data': '2025-08-19T10:25:00.000Z', 'platform': None}, {'id': 38133, 'rank': 5252, 'name': 'Bitcoin AI', 'symbol': 'BTC', 'slug': 'bitcoin-ai', 'is_active': 1, 'status': 1, 'first_historical_data': '2025-08-19T09:45:00.000Z', 'last_historical_data': '2025-08-19T10:30:00.000Z', 'platform': {'id': 14, 'name': 'BNB Smart Chain (BEP20)', 'symbol': 'BNB', 'slug': 'bnb', 'token_address': '0xf22aac87E08d7FC60aA89eb21110ddfE59c20854'}}, {'id': 31652, 'rank': 8148, 'name': 'batcat', 'symbol': 'BTC', 'slug': 'batcat', 'is_active': 1, 'status': 1, 'first_historical_data': '2024-06-06T09:35:00.000Z', 'last_historical_data': '2025-08-19T10:30:00.000Z', 'platform': {'id': 16, 'name': 'Solana', 'symbol': 'SOL', 'slug': 'solana', 'token_address': 'EtBc6gkCvsB9c6f5wSbwG8wPjRqXMB5euptK6bqG1R4X'}}, {'id': 32295, 'rank': 8274, 'name': 'Bullish Trump Coin', 'symbol': 'BTC', 'slug': 'bullish-trump-coin', 'is_active': 1, 'status': 1, 'first_historical_data': '2024-07-19T10:30:00.000Z', 'last_historical_data': '2025-08-19T10:30:00.000Z', 'platform': {'id': 1, 'name': 'Ethereum', 'symbol': 'ETH', 'slug': 'ethereum', 'token_address': '0x43FD9De06bb69aD771556E171f960A91c42D2955'}}, {'id': 34316, 'rank': 8631, 'name': 'HarryPotterTrumpSonic100Inu', 'symbol': 'BTC', 'slug': 'harrypottertrumpsonic100inu', 'is_active': 1, 'status': 1, 'first_historical_data': '2024-11-28T13:40:00.000Z', 'last_historical_data': '2025-08-19T10:30:00.000Z', 'platform': {'id': 1, 'name': 'Ethereum', 'symbol': 'ETH', 'slug': 'ethereum', 'token_address': '0x7099aB9E42Fa7327a6b15E0a0c120c3e50d11BeC'}}, {'id': 30938, 'rank': None, 'name': 'Satoshi Pumpomoto', 'symbol': 'BTC', 'slug': 'satoshi-pumpomoto', 'is_active': 0, 'status': 16, 'platform': {'id': 16, 'name': 'Solana', 'symbol': 'SOL', 'slug': 'solana', 'token_address': '6AGNtEgBE2jph1bWFdyaqsXJ762emaP9RE17kKxEsfiV'}}, {'id': 31469, 'rank': None, 'name': 'Boost Trump Campaign', 'symbol': 'BTC', 'slug': 'boost-trump-campaign', 'is_active': 0, 'status': 16, 'platform': {'id': 1, 'name': 'Ethereum', 'symbol': 'ETH', 'slug': 'ethereum', 'token_address': '0x300e0d87f8c95d90cfe4b809baa3a6c90e83b850'}}]}


# obj = json.dumps(crypto)
# print(obj)
for item in crypto.get("data"):
    crypto_name = item.get("name")
    symbol = item.get("symbol")
    # print(crypto_name, symbol)


import csv

data = json.loads(raw_json)["results"]
with open("domian.csv", "w", newline="", encoding="utf-8") as file:
    w = csv.DictWriter(file, fieldnames=["id", "domain", "tags"])
    w.writeheader()
    for it in data:
        w.writerow({
            "id": it.get("id"),
            "domain": it.get("domain"),
            "tags": "*".join(it.get("tags"))
        })


