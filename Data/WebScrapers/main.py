import pandas as pd
import random

#read csv files:
year = 2020

statsDF = pd.read_csv(r'C:\Projects\NFLPredictor\Data\Test-Data\CombinedStats\CombinedStats'+str(year)+'.csv')

#gameDF = pd.read_csv(r'C:\Projects\NFLPredictor\Data\Train-Data\Games\Games'+str(year)+'.csv')

games = [["Tampa Bay Buccaneers", "Green Bay Packers"], ["Buffalo Bills", "Kansas City Chiefs"]]

team1 = []
team1outcome = []
team1score = []
team1location = []
t1AvgPts = []
t1AvgYads = []
t1NPYA = []
t1NRYA = []
t13rd = []
t14th = []

t1AvgPtsDef = []
t1AvgYadsDef = []
t1NPYADef = []
t1NRYADef = []
t13rdDef = []
t14thDef = []

team2 = []
team2outcome = []
team2score = []
team2location = []
t2AvgPts = []
t2AvgYads = []
t2NPYA = []
t2NRYA = []
t23rd = []
t24th = []

t2AvgPtsDef = []
t2AvgYadsDef = []
t2NPYADef = []
t2NRYADef = []
t23rdDef = []
t24thDef = []


def dePercentify(per):
    num = per.replace('%', '')
    return float(num)/100

for i in range(len(games)):
    teamInfo = []
    #randomly assigns team 1 and team 2
    first = random.randrange(0, 2)
    a = games[i][0]
    b = games[i][1]
    teamInfo.append([a, statsDF.loc[statsDF['Name']==a], 0, 0])
    teamInfo.append([b, statsDF.loc[statsDF['Name']==b], 0, 0])

    teamInfo[0].append('Away')
    teamInfo[1].append('Home')


    #collect all team 1 and team 2 information/stats for each game
    teamOne = teamInfo[first][0]
    teamOneStats = teamInfo[first][1]
    teamTwo = teamInfo[1-first][0]
    teamTwoStats = teamInfo[1-first][1]

    team1.append(teamOne)
    team1outcome.append(teamInfo[first][2])
    team1score.append(teamInfo[first][3])
    team1location.append(teamInfo[first][4])

    t1AvgPts.append(teamOneStats['Avg Points'].item())
    t1AvgYads.append(teamOneStats['Avg Yards'].item())
    t1NPYA.append(teamOneStats['NPY/A'].item())
    t1NRYA.append(teamOneStats['NRY/A'].item())
    t13rd.append(dePercentify(teamOneStats['3rd%_x'].item()))
    t14th.append(dePercentify(teamOneStats['4th%_x'].item()))

    t1AvgPtsDef.append(teamOneStats['Avg Points Let'].item())
    t1AvgYadsDef.append(teamOneStats['Avg Yards Let'].item())
    t1NPYADef.append(teamOneStats['NPY/A Let'].item())
    t1NRYADef.append(teamOneStats['NRY/A Let'].item())
    t13rdDef.append(dePercentify(teamOneStats['3rd%_y'].item()))
    t14thDef.append(dePercentify(teamOneStats['4th%_y'].item()))

    team2.append(teamTwo)
    team2outcome.append(teamInfo[1-first][2])
    team2score.append(teamInfo[1-first][3])
    team2location.append(teamInfo[1 - first][4])

    t2AvgPts.append(teamTwoStats['Avg Points'].item())
    t2AvgYads.append(teamTwoStats['Avg Yards'].item())
    t2NPYA.append(teamTwoStats['NPY/A'].item())
    t2NRYA.append(teamTwoStats['NRY/A'].item())
    t23rd.append(dePercentify(teamTwoStats['3rd%_x'].item()))
    t24th.append(dePercentify(teamTwoStats['4th%_x'].item()))

    t2AvgPtsDef.append(teamTwoStats['Avg Points Let'].item())
    t2AvgYadsDef.append(teamTwoStats['Avg Yards Let'].item())
    t2NPYADef.append(teamTwoStats['NPY/A Let'].item())
    t2NRYADef.append(teamTwoStats['NRY/A Let'].item())
    t23rdDef.append(dePercentify(teamTwoStats['3rd%_y'].item()))
    t24thDef.append(dePercentify(teamTwoStats['4th%_y'].item()))



everything = pd.DataFrame ({
    "T1": team1,
    "T1 Outcome": team1outcome,
    "T1 Score": team1score,
    "T1 Location": team1location,
    "T1 Avg Points": t1AvgPts,
    "T1 Avg Yards": t1AvgYads,
    "T1 NPY/A": t1NPYA,
    "T1 NRY/A": t1NRYA,
    "T1 3rd": t13rd,
    "T1 4th": t14th,
    "T1 Avg Points Def": t1AvgPtsDef,
    "T1 Avg Yards Def": t1AvgYadsDef,
    "T1 NPY/A Def": t1NPYADef,
    "T1 NRY/A Def": t1NRYADef,
    "T1 3rd Def": t13rdDef,
    "T1 4th Def": t14thDef,

    "T2": team2,
    "T2 Outcome": team2outcome,
    "T2 Score": team2score,
    "T2 Location":  team2location,
    "T2 Avg Points": t2AvgPts,
    "T2 Avg Yards": t2AvgYads,
    "T2 NPY/A": t2NPYA,
    "T2 NRY/A": t2NRYA,
    "T2 3rd": t23rd,
    "T2 4th": t24th,
    "T2 Avg Points Def": t2AvgPtsDef,
    "T2 Avg Yards Def": t2AvgYadsDef,
    "T2 NPY/A Def": t2NPYADef,
    "T2 NRY/A Def": t2NRYADef,
    "T2 3rd Def": t23rdDef,
    "T2 4th Def": t24thDef,
})



location = r'C:\Projects\NFLPredictor\Model\AidansModels\Playoffs'
name = '\MatchUp2020ConfChamp'+str(year)+'.csv'
path = location + name
everything.to_csv(path, index=False)


