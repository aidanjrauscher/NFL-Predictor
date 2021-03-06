import pandas as pd
import random


modelNum = 1
year = 1998


path1 = r'C:\Projects\NFLPredictor\Model\model' + str(modelNum) + '.csv'
modelDF = pd.read_csv(path1)

path2 = r'C:\Projects\NFLPredictor\Data\Train-Data\Matchups\MatchUp'+ str(year)  +'.csv'
gameDF = pd.read_csv(path2)

right = 0
wrong = 0
for i in range(len(modelDF["T1"])):
    if gameDF["T1 Outcome"][i] == modelDF['T1 Outcome'][i]:
        right+=1
    else:
        wrong+=1

print(str(round(((right/(right+wrong))*100),3))+"% Accurate")

