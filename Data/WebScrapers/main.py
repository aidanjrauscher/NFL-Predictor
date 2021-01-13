from selenium import webdriver
import pandas as pd

df1 = pd.read_csv(r'C:\Projects\NFLPredictor\Data\Test-Data\OffensiveStats\OffensiveStats2020.csv')
dfa = df1.sort_values(by='Name')
#dfa.set_index('Name', drop=True)
df2 = pd.read_csv(r'C:\Projects\NFLPredictor\Data\Test-Data\OffConvStats\OffConv2020.csv')
dfb = df2.sort_values(by=['Name'])
#dfb.set_index('Name', drop=True)
df3 = pd.read_csv(r'C:\Projects\NFLPredictor\Data\Test-Data\DefensiveStats\DefensiveStats2020.csv')
dfc = df3.sort_values(by=['Name'])
#dfc.set_index('Name', drop=True)
df4 = pd.read_csv(r'C:\Projects\NFLPredictor\Data\Test-Data\DefConvStats\DefConv2020.csv')
dfd = df4.sort_values(by=['Name'])
#dfd.set_index('Name', drop=True)

#allStats = pd.merge(dfa, dfb, dfc, dfd)
allStats = pd.merge(df1.set_index('Name', drop=True),df2.set_index('Name', drop=True), how='left', left_index=True, right_index=True).reset_index()
allStats = pd.merge(allStats.set_index('Name', drop=True),df3.set_index('Name', drop=True), how='left', left_index=True, right_index=True).reset_index()
allStats = pd.merge(allStats.set_index('Name', drop=True),df4.set_index('Name', drop=True), how='left', left_index=True, right_index=True).reset_index()



location = r'C:\Projects\NFLPredictor\Data\Test-Data\CombinedStats'
name = '\CombinedStats2020'
path = location + name
allStats.to_csv(path, index=False)