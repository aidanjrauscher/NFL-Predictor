from selenium import webdriver
import pandas as pd

DRIVER_PATH = 'C:/Projects/Selenium/chromedriver/chromedriver.exe'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)

driver.get('https://www.pro-football-reference.com/years/2020/index.htm')

name = driver.find_elements_by_xpath('/html/body/div[2]/div[5]/div[15]/div[3]/div/table/tbody/tr/td[@data-stat="team"]/a')
third = driver.find_elements_by_xpath("/html/body/div[2]/div[5]/div[15]/div[3]/div/table/tbody/tr/td[@data-stat='third_down_pct']")
fourth = driver.find_elements_by_xpath('/html/body/div[2]/div[5]/div[15]/div[3]/div/table/tbody/tr/td[@data-stat="fourth_down_pct"]')


names = []
per3rd = []
per4th = []


for i in range(len(third)):
    names.append(name[i].text)
    per3rd.append(third[i].text)
    per4th.append(fourth[i].text)

driver.close()

DF = pd.DataFrame ({
    'Name': names,
    '3rd%': per3rd,
    '4th%': per4th,
})

path = r'C:\Projects\NFLPredictor\Data\Test-Data\OffConvStats'
name = "\OffConv2020.csv"
location = path + name
DF.to_csv(location, index=False)





