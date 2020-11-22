""" Checking the weather seems fairly trivial: Open your web browser, click the address bar, type the URL to a weather website (or search for one and then click the link), wait for the page to load, look past all the ads, and so on.

Actually, there are a lot of boring steps you could skip if you had a program that downloaded the weather forecast for the next few days and printed it as plaintext. This program uses the requests module from Chapter 12 (Links to an external site.) to download data from the web.

Overall, the program does the following:

1 Reads the requested location from the command line
2 Downloads JSON weather data from OpenWeatherMap.org
3 Converts the string of JSON data to a Python data structure
4 Prints the weather for today and the next two days
 
So the code will need to do the following:

1 Join strings in sys.argv to get the location.
2 Call requests.get() to download the weather data.
3 Call json.loads() to convert the JSON data to a Python data structure.
4 Print the weather forecast.
For this project, open a new file editor window and save it as getOpenWeather.py. Then visit https://openweathermap.org/api/ (Links to an external site.) in your browser and sign up for a free account to obtain an API key, also called an app ID, which for the OpenWeatherMap service is a string code that looks something like '30144aba38018987d84710d0e319281e'. You don’t need to pay for this service unless you plan on making more than 60 API calls per minute. Keep the API key secret; anyone who knows it can write scripts that use your account’s usage quota. """

import json, requests, sys, csv

APPID = "api key here"

# Compute location from command line arguments.
if len(sys.argv) < 2:
    print('Usage: getOpenWeather.py city_name, 2-letter_country_code')
    sys.exit()    
location = (sys.argv[1])

# Download the JSON data from OpenWeatherMap.org's API.
url ='http://api.openweathermap.org/data/2.5/forecast?q={}&cnt=3&appid={}'.format(location,APPID)
response = requests.get(url)
response.raise_for_status()

# Uncomment to see the raw JSON text:
#print(response.text) 

  # Load JSON data into a Python variable.
weatherData = json.loads(response.text)

   # Print weather descriptions.
w = weatherData['list']
print('Current weather in %s:' % (location))
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('Tomorrow:')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print()
print('Day after tomorrow:')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])
