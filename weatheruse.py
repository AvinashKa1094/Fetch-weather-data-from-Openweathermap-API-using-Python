import requests,json
key = '0293738810e08ff820142045d8b73da6'
url = 'http://api.openweathermap.org/data/2.5/weather?'
city = input('Enter city name :')
complete_url = url+'appid='+ key + '&q=' + city
response = requests.get(complete_url)
x = response.json()
if x["cod"] != "404": 
    y = x["main"] 
    current_temperature = y["temp"] 
    current_pressure = y["pressure"] 
    current_humidiy = y["humidity"] 
    z = x["weather"] 
    weather_description = z[0]["description"] 
    print('Temprature :',str(current_temperature))
    print('Pressure :',str(current_pressure))
    print('Humidiy :',str(current_humidiy))
    print('Description :',str(weather_description))
else:
    print('Please give proper city name ')
