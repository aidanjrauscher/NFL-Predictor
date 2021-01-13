import pandas as pd

df1 = pd.read_csv(r'C:\Projects\NFLPredictor\Data\Train-Data\OffensiveStats\OffensiveStats2011.csv')
dfa = df1.sort_values(by='Name')
#dfa.set_index('Name', drop=True)
df2 = pd.read_csv(r'C:\Projects\NFLPredictor\Data\Train-Data\OffConvStats\OffConv2011.csv')
dfb = df2.sort_values(by=['Name'])
#dfb.set_index('Name', drop=True)
df3 = pd.read_csv(r'C:\Projects\NFLPredictor\Data\Train-Data\DefensiveStats\DefensiveStats2011.csv')
dfc = df3.sort_values(by=['Name'])
#dfc.set_index('Name', drop=True)
df4 = pd.read_csv(r'C:\Projects\NFLPredictor\Data\Train-Data\DefConvStats\DefConv2011.csv')
dfd = df4.sort_values(by=['Name'])
#dfd.set_index('Name', drop=True)


allStats = pd.merge(df1.set_index('Name', drop=True),df2.set_index('Name', drop=True), how='left', left_index=True, right_index=True).reset_index()
allStats = pd.merge(allStats.set_index('Name', drop=True),df3.set_index('Name', drop=True), how='left', left_index=True, right_index=True).reset_index()
allStats = pd.merge(allStats.set_index('Name', drop=True),df4.set_index('Name', drop=True), how='left', left_index=True, right_index=True).reset_index()


location = r'C:\Projects\NFLPredictor\Data\Train-Data\CombinedStats'
name = '\CombinedStats2011'
path = location + name
allStats.to_csv(path, index=False)