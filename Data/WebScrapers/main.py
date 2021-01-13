from selenium import webdriver
import pandas as pd

DRIVER_PATH = 'C:/Projects/Selenium/chromedriver/chromedriver.exe'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)

driver.get('https://www.pro-football-reference.com/years/2013/index.htm')

name = driver.find_elements_by_xpath('/html/body/div[2]/div[5]/div[9]/div[3]/div[2]/table/tbody/tr/td[@data-stat="team"]/a')
gamesPlayed = driver.find_elements_by_xpath("/html/body/div[2]/div[5]/div[9]/div[3]/div[2]/table/tbody/tr/td[@data-stat='g']")
pts = driver.find_elements_by_xpath("/html/body/div[2]/div[5]/div[9]/div[3]/div[2]/table/tbody/tr/td[@data-stat='points']")
yrds = driver.find_elements_by_xpath("/html/body/div[2]/div[5]/div[9]/div[3]/div[2]/table/tbody/tr/td[@data-stat='total_yards']")
npya = driver.find_elements_by_xpath("/html/body/div[2]/div[5]/div[9]/div[3]/div[2]/table/tbody/tr/td[@data-stat ='pass_net_yds_per_att']")
nrya = driver.find_elements_by_xpath("/html/body/div[2]/div[5]/div[9]/div[3]/div[2]/table/tbody/tr/td[@data-stat='rush_yds_per_att']")


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

StatDataFrame1995 = pd.DataFrame ({
    'Name': names,
    'Avg Points': avgPts,
    'Avg Yards': avgYrds,
    'NPY/A': NPYperA,
    'NRY/A': NRYperA,
})

path = r'C:\Projects\NFLPredictor\Data\Train-Data\OffensiveStats'
name = "\OffensiveStats2013.csv"
location = path + name
StatDataFrame1995.to_csv(location, index=False)
