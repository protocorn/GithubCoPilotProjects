#current weather forecast using OpenWeatherMap API by city name
# API key: 7a4b4f4b4b4b4b4b4b4b4b4b4b4b4b4b
# API call: api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
# API call example: api.openweathermap.org/data/2.5/weather?q=London&appid=7a4b4f4b4b4b4b4b4b4b4b4b4b4b4b4b
# API call example: api.openweathermap.org/data/2.5/weather?q=London,uk&appid=7a4b4f4b4b4b4b4b4b4b4b4b4b4b4b4b

import requests
import json
import datetime

# API key
api_key = "126c8babd23dadbca5e0c177619c383c"

# base_url variable to store url

#give user choice between current weather and forecast
print("1. Current Weather")
print("2. Forecast")
choice = input("Enter choice: ")
if(choice != "1" and choice != "2"):
    print("Invalid choice, defaulting to current weather")
    choice = "1"

# Give city name
city_name = input("Enter city name : ")

#ask user their preffered units for temperature
print("1. Kelvin")
print("2. Celsius")
print("3. Fahrenheit")
unit = int(input("Enter choice: "))

if unit != 1 and unit != 2 and unit != 3:
    print("Invalid choice, defaulting to Kelvin")
    unit = 1


# Now x contains list of nested dictionaries
# Check the value of "cod" key is equal to
# "404", means city is found otherwise,
# city is not found
if choice == "1":
    # complete_url variable to store
    # complete url address
    base_url = "http://api.openweathermap.org/data/2.5/weather?" 
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name

    #error handling for api call
    try:
    # get method of requests module
    # return response object
        response = requests.get(complete_url)
    except requests.exceptions.RequestException as e:
        print("Error: " + str(e))
        exit(1)

    # json method of response object
    # convert json format data into
    # python format data
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
        current_humidity = y["humidity"]

        # store the value of "weather"
        # key in variable z
        z = x["weather"]

        # store the value corresponding
        # to the "description" key at
        # the 0th index of z
        weather_description = z[0]["description"]
        if(unit==1):
            current_temperature = current_temperature
            print("Temperature: " + str(current_temperature) + " Kelvin")
        elif(unit==2):
            current_temperature = current_temperature - 273.15
            current_temperature = "{:.2f}".format(current_temperature)
            print("Temperature: " + str(current_temperature) + " Celsius")
        else:
            current_temperature = (current_temperature - 273.15) * (9/5) + 32
            current_temperature = "{:.2f}".format(current_temperature)
            print("Temperature: " + str(current_temperature) + " Fahrenheit")
        # print following values
        print(
              "Pressure: " +
              str(current_pressure) + " hPa"+
              "\nHumidity " +
              str(current_humidity) +   " %"+
              "\nDescription: " +  
              str(weather_description))
        
        #print sunrise and sunset times
        sys = x["sys"]
        sunrise = sys["sunrise"]
        sunrise = datetime.datetime.fromtimestamp(sunrise)
        print("Sunrise: " + sunrise.strftime("%I:%M %p"))
        sunset = sys["sunset"]
        sunset = datetime.datetime.fromtimestamp(sunset)
        print("Sunset: " + sunset.strftime("%I:%M %p"))

    else:
        print(" City Not Found ")
else:
    # complete_url variable to store
    # complete url address
    base_url = "http://api.openweathermap.org/data/2.5/forecast?" 
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name

    try:
        # get method of requests module
        # return response object
        response = requests.get(complete_url)
    except requests.exceptions.RequestException as e:
        print("Error: " + str(e))
        exit(1)

    #give user a choice between specific date and all dates
    print("1. Specific Date")
    print("2. All Dates")
    choice = input("Enter choice: ")

    # json method of response object
    # convert json format data into
    # python format data
    x = response.json()

    #if user chooses all dates
    if choice == "2":
        if x["cod"] != "404":
            # Extract the list of forecasts from the response
            forecasts = x["list"]
            #loop through the list of forecasts
            for forecast in forecasts:
                main = forecast["main"]
                # Extract the temperature from the forecast
                temp = main["temp"]
                # Extract the date from the forecast
                date = forecast["dt_txt"]
                # Convert the date string to a datetime object
                date = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
                # Print the date formatted as "Month, Day Year"
                print(date.strftime("%B %d, %Y"))
                #print the time formatted as "Hour:Minute AM/PM"
                print(date.strftime("%I:%M %p"))
                # Print the temperature
                if(unit==1):
                    temp = temp
                    print("Temperature: " + str(temp) + " Kelvin")
                elif(unit==2):
                    temp = temp - 273.15
                    temp = "{:.2f}".format(temp)
                    print("Temperature: " + str(temp) + " Celsius")
                else:
                    temp = (temp - 273.15) * (9/5) + 32
                    temp = "{:.2f}".format(temp)
                    print("Temperature: " + str(temp) + " Fahrenheit")
                #print the pressure
                pressure = main["pressure"]
                print("Pressure: " + str(pressure)+" hPa")
                #print the humidity
                humidity = main["humidity"]
                print("Humidity: " + str(humidity) + " %")
                #print the wind speed
                wind = forecast["wind"]
                wind_speed = wind["speed"]
                print("Wind Speed: " + str(wind_speed) + " m/s")
                #print the weather description
                weather = forecast["weather"]
                weather_description = weather[0]["description"]
                print("Weather Description: " + str(weather_description))

                #sunrise and sunset times for each day
                if date.hour == 0:
                    sys = x["city"]
                    sunrise = sys["sunrise"]
                    sunrise = datetime.datetime.fromtimestamp(sunrise)
                    print("Sunrise: " + sunrise.strftime("%I:%M %p"))
                    sunset = sys["sunset"]
                    sunset = datetime.datetime.fromtimestamp(sunset)
                    print("Sunset: " + sunset.strftime("%I:%M %p"))
                    print()
                else:
                    print()

        else:
            print(" City Not Found ")
    else:
        #ask user for date for forecast and check that it is in the future and less than 5 days
        date1 = input("Enter date for forecast (YYYY-MM-DD): ")
        date1 = datetime.datetime.strptime(date1, "%Y-%m-%d")
        today = datetime.datetime.today()
        if date1 < today:
            print("Date must be in the future")
        elif date1 > today + datetime.timedelta(days=5):
            print("Date must be less than 5 days in the future")
        else:
            if x["cod"] != "404":
                # Extract the list of forecasts from the response
                forecasts = x["list"]
                #loop through the list of forecasts
                for forecast in forecasts:
                    main = forecast["main"]
                    # Extract the temperature from the forecast
                    temp = main["temp"]
                    # Extract the date from the forecast
                    date = forecast["dt_txt"]
                    # Convert the date string to a datetime object
                    date = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S")

                    if(date1.date()==date.date()):
                        # Print the date formatted as "Month, Day Year"
                        print(date.strftime("%B %d, %Y"))
                        #print the time formatted as "Hour:Minute AM/PM"
                        print(date.strftime("%I:%M %p"))
                        # Print the temperature
                        if(unit==1):
                            temp = temp
                            print("Temperature: " + str(temp) + " Kelvin")
                        elif(unit==2):
                            temp = temp - 273.15
                            temp = "{:.2f}".format(temp)
                            print("Temperature: " + str(temp) + " Celsius")
                        else:
                            temp = (temp - 273.15) * (9/5) + 32
                            temp = "{:.2f}".format(temp)
                            print("Temperature: " + str(temp) + " Fahrenheit")
                        #print the pressure
                        pressure = main["pressure"]
                        print("Pressure: " + str(pressure)+" hPa")
                        #print the humidity
                        humidity = main["humidity"]
                        print("Humidity: " + str(humidity) + " %")
                        #print the wind speed
                        wind = forecast["wind"]
                        wind_speed = wind["speed"]
                        print("Wind Speed: " + str(wind_speed) + " m/s")
                        #print the weather description
                        weather = forecast["weather"]
                        weather_description = weather[0]["description"]
                        print("Weather Description: " + str(weather_description))
                        if date.hour == 0:
                            sys = x["city"]
                            sunrise = sys["sunrise"]
                            sunrise = datetime.datetime.fromtimestamp(sunrise)
                            print("Sunrise: " + sunrise.strftime("%I:%M %p"))
                            sunset = sys["sunset"]
                            sunset = datetime.datetime.fromtimestamp(sunset)
                            print("Sunset: " + sunset.strftime("%I:%M %p"))
                            print()
                        else:
                            print()
            else:
                print(" City Not Found ")
    