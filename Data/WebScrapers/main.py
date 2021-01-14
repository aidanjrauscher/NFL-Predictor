import pandas as pd

df1 = pd.read_csv(r'C:/Projects/NFLPredictor/Data/Train-Data/Matchups/MatchUp2002.csv')
df2 = pd.read_csv(r'C:/Projects/NFLPredictor/Data/Train-Data/Matchups/MatchUp2003.csv')
df3 = pd.read_csv(r'C:/Projects/NFLPredictor/Data/Train-Data/Matchups/MatchUp2004.csv')
df4 = pd.read_csv(r'C:/Projects/NFLPredictor/Data/Train-Data/Matchups/MatchUp2005.csv')
df5 = pd.read_csv(r'C:/Projects/NFLPredictor/Data/Train-Data/Matchups/MatchUp2006.csv')
df6 = pd.read_csv(r'C:/Projects/NFLPredictor/Data/Train-Data/Matchups/MatchUp2007.csv')
df7 = pd.read_csv(r'C:/Projects/NFLPredictor/Data/Train-Data/Matchups/MatchUp2008.csv')
df8 = pd.read_csv(r'C:/Projects/NFLPredictor/Data/Train-Data/Matchups/MatchUp2009.csv')
df9 = pd.read_csv(r'C:/Projects/NFLPredictor/Data/Train-Data/Matchups/MatchUp2010.csv')
df10 = pd.read_csv(r'C:/Projects/NFLPredictor/Data/Train-Data/Matchups/MatchUp2011.csv')
df11 = pd.read_csv(r'C:/Projects/NFLPredictor/Data/Train-Data/Matchups/MatchUp2012.csv')
df12 = pd.read_csv(r'C:/Projects/NFLPredictor/Data/Train-Data/Matchups/MatchUp2013.csv')
df13 = pd.read_csv(r'C:/Projects/NFLPredictor/Data/Train-Data/Matchups/MatchUp2014.csv')
df14 = pd.read_csv(r'C:/Projects/NFLPredictor/Data/Train-Data/Matchups/MatchUp2015.csv')
df15 = pd.read_csv(r'C:/Projects/NFLPredictor/Data/Train-Data/Matchups/MatchUp2016.csv')
df16 = pd.read_csv(r'C:/Projects/NFLPredictor/Data/Train-Data/Matchups/MatchUp2017.csv')
df17 = pd.read_csv(r'C:/Projects/NFLPredictor/Data/Train-Data/Matchups/MatchUp2018.csv')

tet = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11, df12, df13, df14, df15, df16, df17],axis=0)

tet.to_csv('test.csv', index=False)


