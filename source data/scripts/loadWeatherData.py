import urllib.request
import json
import datetime
import sys
import os
import csv
import pandas as pd
import glob


API_KEY = "973ae347af5449d695482859222201"
# -------------------------––––––––-----------
# Get weather data
# -------------------------––––––––-----------

def loadData(years, months, city, country, apikey=API_KEY):
    payload = []

    for year in years:
        for month in months:
            fromDate = datetime.datetime(year, month, 1).strftime("%Y-%m-%d")
            toDate = datetime.datetime(year, month + 1, 1).strftime("%Y-%m-%d")
            url = 'http://api.worldweatheronline.com/premium/v1/past-weather.ashx?key={}&q={}&format=json&date={}&enddate={}' \
                .format(apikey, city, fromDate, toDate)
            payload.append(urllib.request.urlopen(url).read())

    weatherData = []
    for data in payload:
        jsonObject = json.loads(data)
        wheather = jsonObject['data']['weather']
        for w in wheather:

            humiditySum = 0
            humidityCount = 0
            for h in w['hourly']:
                humidityCount += 1
                humiditySum += int(h['humidity'])

            humidityAvg = humiditySum / humidityCount

            obj = [
                country,
                w['date'],
                w['avgtempC'],
                humidityAvg,
                w['hourly'][0]['weatherDesc'][0]['value']
            ]

            weatherData.append(obj)

    savePath = './csv'
    fileName = country.lower() + '.csv'
    completeName = os.path.join(savePath, fileName)

    header = ['country', 'date', 'temp', 'humidity', 'weatherDesc']

    with open(completeName, 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)

        # write the header
        writer.writerow(header)

        # write multiple rows
        writer.writerows(weatherData)


def map_city(country):
    if country == "Czechia":
        return "Prague"
    if country == "Haiti":
        return "Port-Au-Prince"
    if country == "Greece":
        return "Athens"
    if country == "Sweden":
        return "Stockholm"


countries = ["Czechia", "Haiti", "Greece", "Sweden"]

years = [2020, 2021]
months = range(1, 12)
apiKey = ""

try:
    years = [int(x) for x in sys.argv[1].split(",")]
except IndexError:
    years = [2020, 2021]

try:
    months = [int(x) for x in sys.argv[2].split(",")]
except IndexError:
    months = range(1, 12)

try:
    apiKey = sys.argv[3]
except IndexError:
    apiKey = API_KEY

for country in countries:
    city = map_city(country)
    loadData(years, months, city.upper(), country)

extension = 'csv'
all_filenames = [i for i in glob.glob('./csv/*.{}'.format(extension))]
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames])

savePath = '../resultData/'
fileName = "weather" + '.csv'
completeName = os.path.join(savePath, fileName)

combined_csv.rename(columns={'country': 'name', 'temp': 'temperature', 'weatherDesc': 'description'}, inplace=True)

combined_csv.to_csv(completeName, index=False, encoding='utf-8')

# -------------------------––––––––-----------
# Get unique weather description values
# -------------------------––––––––-----------

file = '../resultData/weather.csv'

csv = pd.read_csv(file)
weather_uniq_desc = csv['description'].unique()
df = pd.DataFrame(
    {
        'description': weather_uniq_desc
    }
)

df.to_csv('../resultData/dim_table_weather.csv', index=False)
