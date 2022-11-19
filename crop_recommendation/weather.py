import requests


def weather_fetch(city_name):
    """
    Fetch and returns the temperature and humidity of a city
    :params: city_name
    :return: temperature, humidity
    """
    api_key =   "9d7cde1f6d07ec55650544be1631307e"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    api_response = response.json()

    if api_response["cod"] != "404":
        main_extract = api_response["main"]

        temperature = round((main_extract["temp"] - 273.15), 2)
        humidity = main_extract["humidity"]
        return temperature, humidity
    else:
        return None