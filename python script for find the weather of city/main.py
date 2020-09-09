# python script for find the given city's current weather

import requests
import tkinter as tk
from tkinter import *
from tkinter import messagebox

# labels and entry box of widjet
def CreateWidgets():

    cityLabel = Label(root, text = "Enter City Name : ", bg = "skyblue")
    cityLabel.grid(row = 0, column = 0, padx = 10, pady = 5)

    cityEntry = Entry(root, width = 50, textvariable = cityName)
    cityEntry.grid(row = 0, column = 1, padx = 10, pady = 5)

    findButton = Button(root, text = "Find Weather", command = findWeather)
    findButton.grid(row = 1, column = 0, padx = 5, pady = 5, columnspan = 2)

    cityCoord = Label(root, text = "City Coordinators : ", bg = "skyblue")
    cityCoord.grid(row = 2, column = 0, padx = 10, pady = 5)

    root.cityCoord = Entry(root, width = 50)
    root.cityCoord.grid(row = 2, column = 1, padx = 10, pady = 5)

    tempLabel = Label(root, text = "Temperature : ", bg = "skyblue")
    tempLabel.grid(row = 3, column = 0, padx = 10, pady = 5)

    root.tempEntry = Entry(root, width = 50)
    root.tempEntry.grid(row = 3, column = 1, padx = 10, pady = 5)

    humidityLavel = Label(root, text = "Humidity : ", bg = "skyblue")
    humidityLavel.grid(row = 4, column = 0, padx = 10, pady = 5)

    root.humidityEntry = Entry(root, width = 50)
    root.humidityEntry.grid(row = 4, column = 1, padx= 10, pady = 5)

    windLabel = Label(root, text = "Wind : ", bg = "skyblue")
    windLabel.grid(row = 5, column = 0, padx = 10, pady = 5)

    root.WindEntry = Entry(root, width = 50)
    root.WindEntry.grid(row = 5, column = 1, padx = 10, pady = 5)

    pressureLabel = Label(root, text = "Atmospheric Pressure : ", bg = "skyblue")
    pressureLabel.grid(row = 6, column = 0, padx = 10, pady = 5)

    root.pressureEntry = Entry(root, width = 50)
    root.pressureEntry.grid(row = 6, column = 1, padx = 10, pady = 5)

    descLabel = Label(root, text = "Weather Discription : ", bg = "skyblue")
    descLabel.grid(row = 7, column = 0, padx = 10, pady = 5)

    root.descEntry = Entry(root, width = 50)
    root.descEntry.grid(row = 7, column = 1, padx = 10, pady = 5)

# end of createwidjet function

# find data for entered city
def findWeather():

    # account api key
    APIkey = "0e4a7a2610b3a3413641a759812aa8a6"

    # weather url
    weatherURL = "http://api.openweathermap.org/data/2.5/weather?"

    # storing user input city name
    cityname = cityName.get()

    # storing the complete URL with units = metric ehich means temperature will be shown in celcius
    requestURL = weatherURL + "appid=" + APIkey + "&q=" + cityname + "&units=metric"

    # fetching the result and storing the response
    response = requests.get(requestURL)

    # converting json data format into python
    weatherResponse = response.json()

    # checking if the value of is not equal to 404
    if weatherResponse["cod"] != "404":

        # storing the value of "main" key
        weatherPARA = weatherResponse["main"]

        # storing the value of "coord" key
        coordinates = weatherResponse["coord"]
        latitude = coordinates["lat"]
        longitude = coordinates["lon"]

        # storing the value of "wind" key
        wind = weatherResponse["wind"]
        windSpeed = wind["speed"]
        windDirect = wind["deg"]

        # storing the temperature value which is in kelvin in celcius
        temperature = weatherPARA["temp"]

        # storing the pressure value
        pressure = weatherPARA["pressure"]

        # storing the humidity value
        humidity = weatherPARA["humidity"]

        # storing the weather value from weatherResponse
        weatherDesc = weatherResponse["weather"]

        # storing the value corresponding to the description
        weatherDescription = weatherDesc[0]["description"]

        # printing the results
        root.cityCoord.insert('0', "LATITUDE : " + str(latitude) + "  LONGITUDE : " + str(longitude))
        root.tempEntry.insert('0', str(temperature) + " C")
        root.humidityEntry.insert('0', str(humidity) + " %")
        root.WindEntry.insert('0', "SPEED : " + str(windSpeed) + " meter/sec " + " DIRECTION : " + str(windDirect) + "deg")
        root.pressureEntry.insert('0', str(pressure) + " hPa ")
        root.descEntry.insert('0', weatherDescription)

    # if cod key value is 404 then city is not found
    else:

        messagebox.showerror("ERROR", "CITY NOT FOUND!!")


# end of findweather function

# creating object of window
root = tk.Tk()

# setting the title and backgroung and disabling the resizing property
root.title("Weather Module")
root.resizable(False, False)
root.config(background = "skyblue")

# creating tkinter variable
cityName = StringVar()

# calling the createwidget function
CreateWidgets()

# infinite loop to run application
root.mainloop()