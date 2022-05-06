import requests
import pandas as pd
import io

CSV_URL = "https://covid.ourworldindata.org/data/owid-covid-data.csv"
COUNTRIES = ["Czechia", "Greece", "Sweden", "Haiti"]
DESTINATION_DIRECTORY = "../resultData/covid-19-testing-policy.csv"

with requests.Session() as s:
    r = requests.get(CSV_URL)
    if r.ok:
        data = r.content.decode('utf8')
        df = pd.read_csv(io.StringIO(data))

        filteredCountries = df.loc[df['location'].isin(COUNTRIES)]
        filteredTable = filteredCountries[
            ['iso_code', 'continent', 'location', "date", 'total_cases', 'new_cases', 'new_deaths', 'new_tests',
             'new_vaccinations']]

        df1 = pd.read_csv(DESTINATION_DIRECTORY)
        df1 = df1.loc[df1['Entity'].isin(COUNTRIES)]
        df1.rename(columns={'Entity': 'location', 'Day': 'date', 'Code': 'iso_code'}, inplace=True)

        result = filteredTable.merge(df1)

        result.rename(columns={'location': 'name', 'iso_code': 'code', 'new_cases': 'positive_increase', 'new_deaths': 'number_of_deaths', 'new_tests': 'number_of_tests'}, inplace=True)
        finalResult = result.fillna(0)

        finalResult.to_csv("../resultData/testing-policy.csv", index=False)
