import requests

try:
    url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(url)

    data = response.json()
    print("Vtip:", data["value"])

except Exception:
    print("Chyba pri nacitani API!")
