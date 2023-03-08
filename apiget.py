import requests as re
# pip install requests
# get, post, put, delete

response = re.get("http://api.nbp.pl/api/exchangerates/rates/A/CHF/")
print(response)
# 200 ok
# 4.. błedy
# 5....błedy serwera
table = response.json()
print(table)
print(table['rates'][0]['mid'])

