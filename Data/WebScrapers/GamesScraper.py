from selenium import webdriver
import pandas as pd

DRIVER_PATH = 'C:/Projects/Selenium/chromedriver/chromedriver.exe'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)

driver.get('https://www.pro-football-reference.com/years/1995/games.htm')

weekNum = driver.find_elements_by_xpath("//th[@class='right '][@data-stat='week_num']")
winnerName = driver.find_elements_by_xpath('//td[@data-stat="winner"]')
loserName = driver.find_elements_by_xpath('//td[@data-stat="loser"]')
ptsWinner = driver.find_elements_by_xpath('//td[@data-stat="pts_win"]')
ptsLoser = driver.find_elements_by_xpath('//td[@data-stat="pts_lose"]')
location = driver.find_elements_by_xpath('//td[@data-stat="game_location"]')
dayOfWeek = driver.find_elements_by_xpath('//td[@data-stat="game_day_of_week"]')
timeOfDay = driver.find_elements_by_xpath('//td[@data-stat="gametime"]')

weeks = []
winners = []
winnerPts = []
loserPts = []
losers = []
locations = []
days = []
times = []

for i in range(len(weekNum)):
    week = weekNum[i].text
    try:
        isNum = int(week)
        weeks.append(week)
        winners.append(winnerName[i].text)
        losers.append(loserName[i].text)
        winnerPts.append(ptsWinner[i].text)
        loserPts.append(ptsLoser[i].text)
        locations.append(location[i].text)
        days.append(dayOfWeek[i].text)
        times.append(timeOfDay[i].text)

    except:
        pass
driver.close()

GameDataFrame1995 = pd.DataFrame ({
    'Week': weeks,
    'Winner': winners,
    'Loser' : losers,
    'PtsW': winnerPts,
    'PtsL': loserPts,
    'Location' : locations,
    'Day': days,
    'Time': times,
})

path = r'C:\Projects\NFLPredictor\Data\Train-Data'
name = ""
location = path + name
GameDataFrame1995.to_csv(location, index=False)