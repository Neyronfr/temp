import requests
from django.shortcuts import render
from .models import City

def index(request):
    appid = '0a1ddb1d008cf9a37ce6899405f5e20b'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid
    cities = City.objects.all()
    print(cities)
    all_cities = []
    for city in cities:
        res = requests.get(url.format(city.name)).json()
        city_info = {
        'city': city.name,
        'temp': res["main"]["temp"],
        'icon': res["weather"][0]["icon"]
    }
    all_cities.append(city_info)
    print(all_cities)
    context = {'all_info': all_cities}

    print(context)
    return render(request, 'index.html', {'all_info': all_cities})
