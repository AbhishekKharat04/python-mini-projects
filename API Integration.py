import requests

url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"

try:
    res = requests.get(url, timeout=10)
    res.raise_for_status()

    data = res.json()
    price = data["bitcoin"]["usd"]

    print("Bitcoin price:", price, "USD")

except requests.exceptions.RequestException as e:
    print("API request failed:", e)