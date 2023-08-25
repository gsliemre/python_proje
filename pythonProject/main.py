import requests

def crypto_get():
    response = requests.get("https://raw.githubusercontent.com/atilsamancioglu/K21-JSONDataSet/master/crypto.json")
    if response.status_code==200:
        return response.json()
kripto=crypto_get()
kullanıcı=input("kripto adını giriniz:")
for i in kripto:
    if i["currency"]== kullanıcı:
        print(i["price"])
        break