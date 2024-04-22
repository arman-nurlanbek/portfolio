# Library that has been used for the login system.
import json

# Colors that are used for highlighting and printing essential information:
GREENCOLOR =  '\033[32m'
STANDARDCOLOR = '\033[0m'
BLUECOLOR = '\033[94m'
YELLOWCOLOR = '\033[93m'
REDCOLOR = '\033[91m'

# This function is responsible for running functions "register" and "login"
#      depending on the input given by the players.
# The parameter "player_number_string" represents the number of player using the "login_system" function.
def login_system(player_number_string):
    print("Player " + str(player_number_string) + ":")
    enter = input("Type R to register or L to login: ")
    if enter == "L" or enter == "l":
        return login()
    elif enter == "R" or enter == "r":
        return register()
    else:
        print("Wrong value, please try again")
        return login_system(player_number_string)

# This function is responsible for taking the username and password of the player and
#      by using "authenticate" function checking the inputs in usersdata.json.
def login():
    username = input("Username: ")
    password = input("Password: ")
    if authenticate(username, password):
        print("Congratulations! You have loggen in!")
    else:
        print("No player matches, please try again")
        return login()
    return username

# This function is responsible for checking existance of "Username" and "Password" inputs given
# by the players in usersdata.json
def authenticate(username, password):
    theplayers = loadAccount()
    for player in theplayers:
        if (player['Username'] == username):
            if (player['Password'] == password):
                return True

# The function is responsible for assigning the space for "Username" and "Password" in userdata.json.
def loadAccount():
    with open('usersdata.json') as f:
        theplayers = json.loads(f.read())
        return theplayers


# This function is responsible for registering of new players by taking their "Username" and "Password".
# Then it saves the information in "usersdata.json".
# This function also takes usernames and saves them in "statistics.json" with "wins" and "loses" variables.
def register():
    player = {}
    player['Username'] = input("Username: ")
    player['Password'] = input("Password: ")
    original = loadAccount()
    original.append(player)
    with open('usersdata.json', 'w') as f:
        f.write(json.dumps(original))
    player_stat = {}
    player_stat['Username'] = player['Username']
    player_stat['Wins'] = 0
    player_stat['Loses'] = 0
    statload = loadStats()
    statload.append(player_stat)
    with open('statistics.json', 'w') as s:
        s.write(json.dumps(statload))
        return player['Username']

# This function makes a list of players' usernames with their scores from statistics.json.
def listPlayers():
   statistics = loadStats()
   for score in statistics:
       scores = "{Username} " + GREENCOLOR + "Wins: " + STANDARDCOLOR + "{Wins} " + BLUECOLOR + "Loses: " + STANDARDCOLOR + "{Loses}"
       print (scores.format(**score))

#The function is responsible for assigning the space for "Username" and "Password" in statistics.json.
def loadStats():
    with open('statistics.json') as f:
        statistic = json.loads(f.read())
        return statistic














