import requests
from pprint import pprint as print

API_KEY = '3f83bd03722f8f53e1eaf27d'
currency = "USD"
url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{currency}/UZS"

response = requests.get(url)
#print(response.status_code)
kurs = response.json()['conversion_rate']
print(f"Bugungi kurs: 1AQSH dollori = {kurs} so'm")
