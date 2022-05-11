import requests
import time
import tkinter as tk

def getWeather(canvas):
    city = textfield.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q="+ city +"&appid=e6646298581aaf47e43368f587ba9d7c"
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temperature = int(json_data['main']['temp'] - 273.15)
    minimum_temperature = int(json_data['main']['temp_min'] - 273.15)
    maximum_temperature = int(json_data['main']['temp_max'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    windsp = json_data['wind']['speed']
    sunrise = time.strftime("%H:%M:%S", time.gmtime(json_data['sys']['sunrise'] - 14400))
    sunset = time.strftime("%H:%M:%S", time.gmtime(json_data['sys']['sunset'] - 14400))
    final_info = condition + "\n" + str(temperature) + "°C"
    final_data = "\n" "Max Temp: " + str(maximum_temperature) + "\n" + "Min Temp: " + str(minimum_temperature) +"\n" + "Pressure: " + str(pressure) + "\n" + "Humidity: " + str(humidity) + "\n" + "WindSpeed: " + str(windsp) + "\n" + "Sunrise: " + sunrise + "\n" + "Sunset: " + sunset


    label.config(text = final_info)
    label1.config(text = final_data)

canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("Weather App")
f = ("poppins", 15, "bold")
t = ("poppins", 35, "bold")

textfield = tk.Entry(canvas, font = t)
textfield.pack(pady = 20)
textfield.focus()
textfield.bind('<Return>', getWeather)

label = tk.Label(canvas, font = t)
label.pack()
label1 = tk.Label(canvas, font= f)
label1.pack()

resp = requests.get('https://facebook.com/')
print(resp)
print(resp.status_code)
print(resp.headers)
print(resp.headers['Content-Type'])
print(resp.text)
canvas.mainloop()

