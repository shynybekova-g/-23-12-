from django.shortcuts import render
import requests
from urllib.parse import quote_plus
from django.conf import settings

def index(request):
    weather_data = None
    error = None

    if request.method == 'POST':
        city = request.POST.get('city')
        if city:
            # settings.py-дан API_KEY алу
            api_key = settings.OPENWEATHERMAP_API_KEY
            city_encoded = quote_plus(city)
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city_encoded}&appid={api_key}&units=metric&lang=en"

            try:
                response = requests.get(url)
                data = response.json()

                if data.get("cod") == 200:
                    weather_data = {
                        "city": data["name"],
                        "temperature": round(data["main"]["temp"]),
                        "description": data["weather"][0]["description"],
                        "icon": f"http://openweathermap.org/img/wn/{data['weather'][0]['icon']}.png"
                    }
                else:
                    error = f"Error: {city}. Атын ағылшынша енгізіңіз (мысалы, Almaty)."
            except Exception as e:
                error = f"Серверде қате шықты: {e}"
        else:
            error = "Қала енгізілмеген."

    return render(request, "weather/index.html", {"weather": weather_data, "error": error})