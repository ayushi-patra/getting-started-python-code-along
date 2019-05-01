# --------------
import yaml

# Read the data of the format .yaml type
with open(path, 'r') as f:
     doc = yaml.load(f) 

# Find data type of the file
print((type(cricdata))) # stores the data about one match

# In which city, and at which venue the match was played and where was it played ?
venue = cricdata['info']['venue']
city = cricdata['info']['city']

print('Match was played at {} in {}'.format(venue,city)) 

# Which are all the teams that played in the tournament ? How many teams participated in total?
teams = cricdata['info']['teams']
n_teams = len(teams) 
print('The teams that played in the tournament are {}and the total number of teams participated are {}'.format(teams, n_teams)) 

# Which team won the toss and what was the decision of toss winner ?
winner = cricdata['info']['toss']['winner']
decision = cricdata['info']['toss']['decision']
print('{} won the toss and decided to {} first'.format(winner,decision)) 

# Find the first bowler and first batsman who played the first ball of the first inning
# print(type(cricdata['innings'])) 

first_innings_info = cricdata['innings'][0]['1st innings']
#print(first_innings_info) 
first_innings_first_ball_bowler = first_innings_info['deliveries'][0][0.1]['bowler']

first_innings_first_ball_batsman = first_innings_info['deliveries'][0][0.1]['batsman']

print('The first bowler who played the first ball of the first inning is {} and the first batsman who faced first delivery is {}'.format(first_innings_first_ball_bowler,first_innings_first_ball_batsman)) 

# How many deliveries were delivered in first inning ?
Number_of_deliveries_1stinnings = len(first_innings_info['deliveries'])
print('{} were bowled in the first innings'.format(Number_of_deliveries_1stinnings)) 

# max_valid_deliveries = 120
# print('{} extras were bowled in the first innings'.format(Number_of_deliveries - max_valid_deliveries))

# How many deliveries were delivered in second inning ?
second_innings_info = cricdata['innings'][1]['2nd innings']
Number_of_deliveries_2ndinnings = len(second_innings_info['deliveries']) 
print('{} were bowled in the second innings'.format(Number_of_deliveries_2ndinnings)) 

# Which team won and how ?

winner = cricdata['info']['outcome']['winner']
how_win = cricdata['info']['outcome']['by'] 
value_win = list(how_win.values())[0] # number of wickets or number of runs 
mode_of_win = list(how_win.keys())[0] # runs/wickets
print('{} won by {} {}'.format(winner, mode_of_win, value_win))  



