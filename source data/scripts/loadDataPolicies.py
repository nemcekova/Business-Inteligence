from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys
import pandas as pd

URL_TESTING = "https://ourworldindata.org/grapher/covid-19-testing-policy"
URL_MASKS = "https://ourworldindata.org/grapher/face-covering-policies-covid"
URL_TRAVEL = "https://ourworldindata.org/grapher/international-travel-covid"
URL_STAY_HOME = "https://ourworldindata.org/grapher/stay-at-home-covid"
URL_EVENTS = "https://ourworldindata.org/grapher/public-gathering-rules-covid"
URL_SCHOOLS = "https://ourworldindata.org/grapher/school-closures-covid"
URL_WORKPLACE = "https://ourworldindata.org/grapher/workplace-closures-covid"

COUNTRIES = ["Czechia", "Greece", "Sweden", "Haiti"]

urls = [URL_TESTING, URL_MASKS, URL_STAY_HOME, URL_TRAVEL, URL_EVENTS, URL_WORKPLACE, URL_SCHOOLS]

path = ""

try:
    path = sys.argv[1]
except IndexError:
    path = "/Users/burianl/Projects/Avast/BIDS/source data/resultData"

op = webdriver.ChromeOptions()
p = {"download.default_directory": path}
op.add_experimental_option("prefs", p)

browser = webdriver.Chrome('/Users/burianl/Downloads/chromedriver', chrome_options=op)
wait = WebDriverWait(browser, 10)

for page in urls:
    browser.get(page)

    # wait for page to load
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'GrapherComponent')))

    browser.find_element_by_xpath("//a[text()=' Download']").click()

    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'grouped-menu-item')))
    browser.find_element_by_xpath("//button[@data-track-note = 'chart-download-csv']").click()

    time.sleep(3)

browser.quit()

files = [
    'face-covering-policies-covid.csv',
    'international-travel-covid.csv',
    'public-gathering-rules-covid.csv',
    'school-closures-covid.csv',
    'stay-at-home-covid.csv',
    'workplace-closures-covid.csv'
]

result = pd.read_csv('../resultData/' + files[0])
fc = result.loc[result['Entity'].isin(COUNTRIES)]

result = pd.read_csv('../resultData/' + files[1])
it = result.loc[result['Entity'].isin(COUNTRIES)]

result = pd.read_csv('../resultData/' + files[2])
pg = result.loc[result['Entity'].isin(COUNTRIES)]

result = pd.read_csv('../resultData/' + files[3])
schc = result.loc[result['Entity'].isin(COUNTRIES)]

result = pd.read_csv('../resultData/' + files[4])
sah = result.loc[result['Entity'].isin(COUNTRIES)]

result = pd.read_csv('../resultData/' + files[5])
wc = result.loc[result['Entity'].isin(COUNTRIES)]

result = fc.merge(it)
result = result.merge(pg)
result = result.merge(schc)
result = result.merge(sah)
result = result.merge(wc)

result.rename(columns={'Entity': 'name', 'Day': 'date', 'Code': 'code', 'facial_coverings': 'masks',
                       'international_travel_controls': 'type_travel_controle',
                       'restriction_gatherings': 'public_events',
                       'school_closures': 'closure_schools', 'stay_home_requirements': 'stay_at_home',
                       'workplace_closures': 'closure_workplace'},
              inplace=True)

finalResult = result.fillna(0)

finalResult.to_csv("../resultData/restrictions.csv", index=False)
