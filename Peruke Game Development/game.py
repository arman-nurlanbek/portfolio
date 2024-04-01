# game.py
# Peruke game. Student ID: u2191382.

# Libraries that has been used for the game:
import random
from datetime import datetime
import json

# This command imports "login_system" function from loginsystem.py
from login_system import login_system
from login_system import listPlayers


# Colors that are used for highlighting and printing essential information:
GREENCOLOR =  '\033[32m'
STANDARDCOLOR = '\033[0m'
BLUECOLOR = '\033[94m'
YELLOWCOLOR = '\033[93m'
REDCOLOR = '\033[91m'

# Keys of dictionaries are used as disks for the game.
# "True" value means that a disk is defended. "False" value means a disk is not defended.
# All values are set as "not defended" by the default.
dictionary_1 = {1: False, 2: False, 3: False, 4: False, 5: False, 6: False}
dictionary_2 = {1: False, 2: False, 3: False, 4: False, 5: False, 6: False}
dictionary_list_1 = list(dictionary_1.keys())
dictionary_list_2 = list(dictionary_2.keys())
player_1 = ''
player_2 = ''

#loginsystem.py

# Library that has been used for the login system.
import json

#loginsystem.py

# Library that has been used for the login system.
import json


# The function "attacker" is responsible for attacking actions.
# The parameter "attacked_player" represents player who is under attack.
# The parameter "attacking_player" represents player who is attacking.
# The parameter "taken_random_number" is the number that is taken every round from the function "inside_the_game".
def attacker(attacked_player,attacking_player, taken_random_number):
    while True:
        if taken_random_number in list(attacked_player.keys()) and attacked_player[taken_random_number] == False:
          del attacked_player[taken_random_number]
          break
        if taken_random_number in list(attacked_player.keys()) and attacked_player[taken_random_number] == True:
          attacked_player[taken_random_number] = False
          break
        else:
          break
    return attacked_player,attacking_player, taken_random_number

# The function "defender" is responsible for defending actions.
# The parameter "defending_player" represents player who is able to defend their disk.
# The parameter "attacked_player" represents player who is under attack.
# The parameter "taken_random_number" is the number that is taken every round from the function "inside_the_game".
def defender(defending_player,attacked_player, taken_random_number):
    while True:
        if taken_random_number in list(defending_player.keys()) and defending_player[taken_random_number] == False:
            defending_player[taken_random_number] = True
            break
        if taken_random_number in list(defending_player.keys()) and defending_player[taken_random_number] == True:
            break
        else:
            break
    return defending_player,attacked_player, taken_random_number

# The function "inside_game_function" is responsible for cooperation of "attacker" and "defending" functions
#     which depend on the input given by the players and status of heir disks in the present round.
# The parameters "acting_player_first" and "acting_player_second" represent players who are capable of certain function
#     depending on each round.
# The parameter "number_of_acting_player" represents the player who is capable of certain functions
#     depending on each round.
def inside_game_function(acting_player_first, acting_player_second, number_of_acting_player):
    random_number = random.randint(1, 6)
    while dictionary_list_1 or dictionary_list_2 != []:
        print("Your random number is " + BLUECOLOR + str(random_number) + STANDARDCOLOR)
        action = input("Choose Attack or Defense: ")
        print("---------------------------------------")
        if action == "a" and random_number in acting_player_second:
            attacker(acting_player_second, acting_player_first, random_number)
            break
        if action == "d" and random_number in acting_player_first:
            defender(acting_player_first, acting_player_second, random_number)
            break
        if (action != "a" and action != "d") and (random_number in acting_player_first or random_number in acting_player_second):
            print(REDCOLOR + "Wrong Button! Try again." + STANDARDCOLOR)
            continue
        if action != "a" and action != "d" and (random_number not in acting_player_first and random_number not in acting_player_second):
            break
        if action == "a" and random_number not in acting_player_second and random_number in acting_player_first:
            print(REDCOLOR + "You can only defend" + STANDARDCOLOR)
            continue
        if action == "d" and random_number not in acting_player_first and random_number in acting_player_second:
            print(REDCOLOR + "You can only attack" + STANDARDCOLOR)
            continue
        if (action == "a" or action == "d") and random_number not in acting_player_first and random_number not in acting_player_second:
            print(REDCOLOR + "You can neither attack nor deffense. Press Enter")
            continue
    print("Discs of Player 1: " + str(list(dictionary_1.keys())))
    print("Discs of Player 2: " + str(list(dictionary_2.keys())))
    print(GREENCOLOR + "Defended " + STANDARDCOLOR + "discs of Player " + str(number_of_acting_player) + ":")
    for keys, values in acting_player_first.items():
        if True == values:
            print(GREENCOLOR + f"[{str(keys)}]" + STANDARDCOLOR)
    return dictionary_1, dictionary_2, dictionary_list_1, dictionary_list_2, number_of_acting_player

# The major function "game_function" is responsible for operation and run of the "login_system"
#     function and shuffle of the function "inside_game_function" depending on progress
#     order between players.
# The "game_function" also reads the current conditions of the disks of the player
#     until by the end of some round one or both of the players dictionaries are empty.
# After the end of the game the function adds wins or loses in statistics.json and prints
# current score of all players.

def game_function():
    username1 = login_system(1)
    username2 = login_system(2)
    print(username1, username2)
    print("Discs of Player 1 :" + str(dictionary_list_1))
    print("Discs of Player 2 :" + str(dictionary_list_2))
    while True:
        print(YELLOWCOLOR + "It is Player 1 turn" + STANDARDCOLOR)
        inside_game_function(dictionary_1, dictionary_2, "1")
        print(YELLOWCOLOR + "It is Player 2 turn" + STANDARDCOLOR)
        inside_game_function(dictionary_2, dictionary_1, "2")
        with open('statistics.json') as file:
            data = json.load(file)
        if len(list(dictionary_1.keys())) == 0:
            print("Congratulations!")
            print(REDCOLOR + "Winner is Player 2" + STANDARDCOLOR)

            for item in data:
                if username2 == item['Username']:
                    item['Wins'] += 1

                if username1 == item['Username']:
                    item['Loses'] += 1


            with open('statistics.json', 'w') as file:
                json.dump(data, file, indent=2)
            listPlayers()

        if len(list(dictionary_2.keys())) == 0:
            print("Congratulations!")
            print(REDCOLOR + "Winner is Player 1" + STANDARDCOLOR)
            for item in data:
                if username1 == item['Username']:
                    item['Wins'] += 1

                if username2 == item['Username']:
                    item['Loses'] += 1

            with open('statistics.json', 'w') as file:
                json.dump(data, file, indent=2)
            listPlayers()

            break
        if len(list(dictionary_1.keys())) == 0 and len(list(dictionary_2.keys())) == 0:
            print("Fair game. Draw.")



# This command prints the greeting and functionality of the game.
print("""
Welcome to the""" + GREENCOLOR + " Peruke Game!" + STANDARDCOLOR +
"""
Type """ + REDCOLOR + 'a ' + STANDARDCOLOR + "to Attack" +
"""
Type""" + REDCOLOR + ' b ' + STANDARDCOLOR + "to Defense" +
"""
If you do not have move options during the game - Press """ + REDCOLOR + "Enter" + STANDARDCOLOR)

# This command waits for the input to start the game.
start_of_the_game = input("""Press Enter now to start the game... """)
# This command saves the time right before the game starts.
time_of_beggining_of_the_game = datetime.now()
# This runs "game_function" function.
game_function()
# This command saves the time right after the game ends.
time_of_end_of_the_game = datetime.now()
# This command counts the time the whole game has taken.
time_the_game_played = time_of_end_of_the_game - time_of_beggining_of_the_game
# This command prints the time the whole game has taken.
print(BLUECOLOR + "You played for " + STANDARDCOLOR + str(time_the_game_played))













