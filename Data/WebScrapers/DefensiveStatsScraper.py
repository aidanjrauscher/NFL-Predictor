from selenium import webdriver
import pandas as pd

DRIVER_PATH = 'C:/Projects/Selenium/chromedriver/chromedriver.exe'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)

driver.get('https://www.pro-football-reference.com/years/1995/opp.htm')

name = driver.find_elements_by_xpath('//td[@data-stat="team"]')
gamesPlayed = driver.find_elements_by_xpath("/html/body/div[2]/div[5]/div[2]/div[2]/div/table/tbody/tr/td[@data-stat='g']")
pts = driver.find_elements_by_xpath('/html/body/div[2]/div[5]/div[2]/div[2]/div/table/tbody/tr/td[@data-stat="points"]')
yrds = driver.find_elements_by_xpath("//*[@id='team_stats']/tbody/tr/td[@data-stat='total_yards']")
npya = driver.find_elements_by_xpath("//*[@id='team_stats']/tbody/tr/td[@data-stat ='pass_net_yds_per_att']")
nrya = driver.find_elements_by_xpath("//*[@id='team_stats']/tbody/tr/td[@data-stat='rush_yds_per_att']")

names = []
avgPts = []
avgYrds = []
NPYperA = []
NRYperA = []



for i in range(len(pts)):
    games = int(gamesPlayed[i].text)
    names.append(name[i].text)
    avgPts.append(int(pts[i].text)/games)
    avgYrds.append(int(yrds[i].text)/games)
    NPYperA.append(float(npya[i].text))
    NRYperA.append(float(nrya[i].text))

driver.close()

DF = pd.DataFrame ({
    'Name': names,
    'Avg Points Let': avgPts,
    'Avg Yards Let': avgYrds,
    'NPY/A Let': NPYperA,
    'NRY/A Let': NRYperA,
})

path = r'C:\Projects\NFLPredictor\Data\Train-Data'
name = "\DefensiveStats1995.csv"
location = path + name
DF.to_csv(location, index=False)
