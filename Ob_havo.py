import requests, json

api_key = "3b6ac6966cf8d5d4f86ebd4cc8e0d5ec"
base_url = "https://api.openweathermap.org/data/2.5/weather?"

city_name = input("Enter your city: ")
complete_url = base_url + "q=" + city_name + "&appid=" + api_key

response = requests.get(complete_url)
x = response.json()

if x["cod"]!="404":
    y = x["main"]
    current_temperature = y["temp"]
    current_pressure = y["pressure"]
    current_humidity = y["humidity"]
    current_name = x["name"]
    current_country = x["sys"]["country"]

    z = x["weather"]
    weather_description = z[0]["description"]
    print("Country = " + str(current_country) + "\nLocation = " + str(current_name) + "\nTemperature(harorat) = " + str(current_temperature) + "\n Pressure(bosim) = " + str(current_pressure) + "\n Humidity(namlik) =  " + str(current_humidity) + " %" + "\n Description(tavsif) = " + str(weather_description))
else:
    print("City not found")
