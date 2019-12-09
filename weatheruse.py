import requests,json
key = '0293738810e08ff820142045d8b73da6'
url = 'http://api.openweathermap.org/data/2.5/weather?'
city = input('Enter city name :')
complete_url = url+'appid='+ key + '&q=' + city
response = requests.get(complete_url)
x = response.json()
if x["cod"] != "404": 
  
    # store the value of "main" 
    # key in variable y 
    y = x["main"] 
  
    # store the value corresponding 
    # to the "temp" key of y 
    current_temperature = y["temp"] 
  
    # store the value corresponding 
    # to the "pressure" key of y 
    current_pressure = y["pressure"] 
  
    # store the value corresponding 
    # to the "humidity" key of y 
    current_humidiy = y["humidity"] 
  
    # store the value of "weather" 
    # key in variable z 
    z = x["weather"] 
  
    # store the value corresponding  
    # to the "description" key at  
    # the 0th index of z 
    weather_description = z[0]["description"] 

    print('Temprature :',str(current_temperature))
    print('Pressure :',str(current_pressure))
    print('Humidiy :',str(current_humidiy))
    print('Description :',str(weather_description))
else:
    print('Please give proper city name ')
