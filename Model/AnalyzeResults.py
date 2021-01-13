import pandas as pd
import random

#read csv files:

modelDF = pd.read_csv(r'C:\Projects\NFLPredictor\Data\Model\model1.csv')

gameDF = pd.read_csv(r'C:\Projects\NFLPredictor\Data\Train-Data\Matchups\MatchUp1998.csv')

right = 0
wrong = 0
for i in range(len(modelDF["T1"])):
    if gameDF["T1 Outcome"][i] == modelDF['T1 Outcome'[i]]:
        right+=1
    else:
        wrong+=1

print(str((right/(right+wrong))*100)+"%")



