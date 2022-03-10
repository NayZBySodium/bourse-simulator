import request;

API_KEY = "secret"
API_URL = "http://api.marketstack.com"
DATE = "2022-10-03"
SYMBOLS = "AAPL"

r = request.get(API_URL + "/intraday/" + DATE + "?symbols=" + SYMBOLS + "&access_key=" + API_KEY))

print(r)
