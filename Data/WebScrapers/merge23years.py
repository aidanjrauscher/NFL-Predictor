import pandas as pd

df1 = pd.read_csv(r'C:/Projects/NFLPredictor/Data/Train-Data/Matchups/MatchUp1996.csv')
df2 = pd.read_csv(r'C:/Projects/NFLPredictor/Data/Train-Data/Matchups/MatchUp1997.csv')
df3 = pd.read_csv(r'C:/Projects/NFLPredictor/Data/Train-Data/Matchups/MatchUp1998.csv')
df4 = pd.read_csv(r'C:/Projects/NFLPredictor/Data/Train-Data/Matchups/MatchUp1999.csv')
df5 = pd.read_csv(r'C:/Projects/NFLPredictor/Data/Train-Data/Matchups/MatchUp2000.csv')
df6 = pd.read_csv(r'C:/Projects/NFLPredictor/Data/Train-Data/Matchups/MatchUp2001.csv')
df7 = pd.read_csv(r'C:/Projects/NFLPredictor/Data/WebScrapers/testNOPERCENTAGES.csv')

tet = pd.concat([df1, df2, df3, df4, df5, df6, df7],axis=0)

tet.to_csv('test.csv', index=False)