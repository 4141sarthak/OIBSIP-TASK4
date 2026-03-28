import requests

API_KEY = "37b99d24a18e4e249db204546262803"

def fetch_weather(city):
    try:
        url = f"http://api.weatherapi.com/v1/forecast.json?key={API_KEY}&q={city}&days=7"
        
        response = requests.get(url)

        if response.status_code != 200:
            print("HTTP Error:", response.status_code)
            return None

        data = response.json()

        if "error" in data:
            print("API Error:", data["error"])
            return None

        return data

    except Exception as e:
        print("Exception:", e)
        return None