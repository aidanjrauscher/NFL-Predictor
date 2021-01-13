# Data Guide 

### Explanation of Collected Data 
All data falls into five categories, and represents game information and stats from 1994 to 2020. 

The five categories of data collected are as follows:
1. Games: week, winner, loser, score, location, day of week, time
2. Season Offenive Stats for Each Team: team, avg points, avg yards, net yards gained per pass attempt, and rushing yards gained per attempt
3. Season Offensive Conversion Stats for Each Team: team, 3rd down conversion %, 4th down conversion %
4. Season Defensive Stats for Each Team: team, avg points allowed, avg yards allowed, net yards allowed per pass attempt, and rushing yards aallowed per attempt
5. Season Defensive Conversion Stats for Each Team: team, 3rd down conversion % allowed, 4th down conversion % allowed

The model will be trained with data from 1995 to 2018 for ther following reasons: 
1. From 1995 on there were at least 30 teams in the NFL for any given season.
2. From 1995 on the average number of points scored per team per game never fell below 20 for any given season. 

### Collection of Data
All data was collected with a set of scrapers utilizing the selenium and pandas packages. 

### Source
All data has been scraped from <a href='https://www.pro-football-reference.com/'> _**Pro Football Reference**_ </a>. 
