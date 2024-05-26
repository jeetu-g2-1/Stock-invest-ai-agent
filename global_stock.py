
url = 'https://www.alphavantage.co/query?function=NEWS_SENTIMENT&tickers=AAPL&apikey=1HRCG3M2TLBM8PIS'
r = requests.get(url)
data = r.json()

print(data)
