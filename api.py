import requests

def get_joke():

    try:
        response = requests.get("https://official-joke-api.appspot.com/random_joke")

        data = response.json()

        print(data["setup"])
        print(data["punchline"])

    except requests.RequestException:
        print("Chyba při načítání API")


get_joke()
