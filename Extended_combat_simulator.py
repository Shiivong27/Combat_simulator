class Unit:                    # a class unit defined to return the 'type' of the unit
    def __init__(self, type):  # which is passed to the who_wins function to determine the winner
        self.__type__ = type

    def get_type(self):
        return self.__type__


print("Welcome, Commaders! Time to make your army.")

print("\nEach player has $10 each to make an army of 10 units which cost $1 each.\n")

num_players_playa1 = int(input("Enter the number of players for Player 1: "))       # Player 1 input

num_players_playa2 = int(input("\nEnter the number of players for Player 2: "))     # Player 2 input

knight = Unit("knight")     # creating class objects for each of the units
archer = Unit("archer")
soldier = Unit("soldier")
siege_equipment = Unit("siege equipment")
wizard = Unit("wizard")

unit_options = [soldier, knight, archer, siege_equipment, wizard]       # a list of units for the players to choose from


def who_wins(unit1, unit2):     # all the game rules defined in one function

    if unit1.get_type() == unit2.get_type():
        return 'tie'

    elif unit1.get_type() == 'archer' and unit2.get_type() == 'soldier':
        return 'archer'

    elif unit1.get_type() == 'archer' and unit2.get_type() == 'knight':
        return 'knight'

    elif unit1.get_type() == 'archer' and unit2.get_type() == 'wizard':
        return 'archer'

    elif unit1.get_type() == 'archer' and unit2.get_type() == 'siege equipment':
        return 'siege equipment'

    elif unit1.get_type() == 'soldier' and unit2.get_type() == 'archer':
        return 'archer'

    elif unit1.get_type() == 'soldier' and unit2.get_type() == 'knight':
        return 'soldier'

    elif unit1.get_type() == 'soldier' and unit2.get_type() == 'wizard':
        return 'wizard'

    elif unit1.get_type() == 'soldier' and unit2.get_type() == 'siege equipment':
        return 'siege equipment'

    elif unit1.get_type() == 'knight' and unit2.get_type() == 'archer':
        return 'knight'

    elif unit1.get_type() == 'knight' and unit2.get_type() == 'soldier':
        return 'soldier'

    elif unit1.get_type() == 'knight' and unit2.get_type() == 'wizard':
        return 'wizard'

    elif unit1.get_type() == 'knight' and unit2.get_type() == 'siege equipment':
        return 'knight'

    elif unit1.get_type() == 'wizard' and unit2.get_type() == 'archer':
        return 'archer'

    elif unit1.get_type() == 'wizard' and unit2.get_type() == 'soldier':
        return 'wizard'

    elif unit1.get_type() == 'wizard' and unit2.get_type() == 'knight':
        return 'wizard'

    elif unit1.get_type() == 'wizard' and unit2.get_type() == 'siege equipment':
        return 'wizard'

    elif unit1.get_type() == 'siege equipment' and unit2.get_type() == 'archer':
        return 'siege equipment'

    elif unit1.get_type() == 'siege equipment' and unit2.get_type() == 'soldier':
        return 'siege equipment'

    elif unit1.get_type() == 'siege equipment' and unit2.get_type() == 'knight':
        return 'knight'

    elif unit1.get_type() == 'siege equipment' and unit2.get_type() == 'wizard':
        return 'wizard'


def get_number_input(prompt_message):       # this function prevents the program from crashing when only enter
    try:                                    # is given as the input, by prompting for a re-enter from the user
        return int(input(prompt_message))
    except:
        print("Please enter a valid option as number")
        return get_number_input(prompt_message)


def combat(playa1, playa2):     # this function decides and displays the winner of each round

  num_of_playa1 = num_players_playa1        # this initialization is done to overcome 'unresolved reference' problem
  num_of_playa2 = num_players_playa2

  while num_of_playa1 > 0 and num_of_playa2 > 0:      # while both players have at-least 1 player in their team

    num_of_playa1 = num_of_playa1 -1        # decrementing number of units after
    num_of_playa2 = num_of_playa2 -1        # each loop iteration

    score_playa1 = 0        # initializing player scores as zero
    score_playa2 = 0

    num_playa1_medics = 10 - len(playa1)        # computing the no. of medics left for each player
    num_playa2_medics = 10 - len(playa2)

    num_playa1_medics_used = 0      # keeping a track of medics used by each player
    num_playa2_medics_used = 0

    playa1_index = 0        # iterative index to determine the unit in each players list
    playa2_index = 0

    print("COMBAT RESULTS FOR ALL ROUNDS")      # just for a better display :)
    print("****** ******* *** *** ******")

    while playa1_index < 10 and playa2_index < 10:      # loop till all the 10 units of each players are exhausted


        unit1 = playa1[playa1_index]        # a variable which holds the unit information
        unit2 = playa2[playa2_index]        # for each player's list

        if who_wins(unit1, unit2) == unit1.get_type():      # fetching the results of the combat and declaring the round winner
            print("Player 1's " + unit1.get_type() + " wins against Player 2's " + unit2.get_type() + "!")


            if num_playa2_medics > num_playa2_medics_used:      # condition to check if medics are still available
                print("Player 2's medic revived the fallen " + unit2.get_type())
                num_playa2_medics_used += 1     # incrementing medics used if it revives a unit
                playa2.append(unit2)        # appending the unit back into the list
            playa2_index += 1       # incrementing player index
            score_playa1 += 1       # incrementing player score

        elif who_wins(unit1, unit2) == unit2.get_type():        # fetching the results of the combat and declaring the round winner
            print("Player 2's " + unit2.get_type() + " wins against Player 1's " + unit1.get_type() + "!")

            if num_playa1_medics > num_playa1_medics_used:      # condition to check if medics are still available
                print("Player 1's medic revived the fallen " + unit1.get_type())
                num_playa1_medics_used += 1     # incrementing medics used if it revives a unit
                playa1.append(unit1)        # appending the unit back into the list
            playa1_index += 1       # incrementing player index
            score_playa2 += 1       # incrementing player score

        else:
            print("tie")        # in case of a tie, the same procedure is repeated and
                                #the player index and medics used are incremented

            if num_playa2_medics > num_playa2_medics_used:
                print("Player 2's medic revived the fallen " + unit2.get_type())
                num_playa2_medics_used += 1
                playa2.append(unit2)
            playa2_index += 1

            if num_playa1_medics > num_playa1_medics_used:
                print("Player 1's medic revived the fallen " + unit1.get_type())
                num_playa1_medics_used += 1
                playa1.append(unit1)
            playa1_index += 1
            continue        # returns control to the beginning of the loop

    if score_playa1 > score_playa2:     # comparing the final scores of both players
        print("\nPlayer 1 Wins!")       # and displaying the result

    elif score_playa2 > score_playa1:
        print("\nPlayer 2 Wins!")

    else:
        print("\nOh boy it's a Tie!!")
    print("\nPlayer 1 final score: " + str(score_playa1) + "\n" + "\nPlayer 2 final score: " + str(score_playa2))

  if num_players_playa1 == 0 and num_players_playa2 == 0:       # error handling to check if both players choose zero units
     print("Game Over! Why did you not choose any players? :(")

  elif num_players_playa1 > 0 and num_players_playa2 == 0:      # if one player chooses zero units and the other chooses
       print("Player 1 wins by default!")                       # non-zero units, then the former wins by default
  elif num_players_playa1 == 0 and num_players_playa2 > 0:
       print("Player 2 wins by default!")
  else:
       print("")




def get_playa1_unit_list(num_players_playa1):

    unit_list = []      # initializing an empty list

    playa1_money_left = num_players_playa1 - 1      # computing the money left for medics after Player 2's army creation
    print("\nWelcome, Player 1. Time to choose your army now. May the force be with you!")

    for i in range(num_players_playa1):     # looping over the number of units
        unit_type = -1
        incorrect_entered = False       # flag is set to false when valid number for unit is entered

        while unit_type < 1 or unit_type > 5:       # while the unit is between 1 and 5
            if incorrect_entered:
                print("Choose only valid inputs : 1, 2, 3, 4 or 5")     # error handling for invalid inputs

            unit_type = get_number_input(       # fetching the unit type from the player
                "Press 1 to add Soldier, 2 to add Knight, 3 to add an Archer, 4 to add Siege Equipment and 5 to add Wizard: ")

            incorrect_entered = True        # flag is set to true when an invalid input is given by the player
        print("Money left : " + str(playa1_money_left))     # printing the money left
        playa1_money_left = playa1_money_left - 1       # decrementing the money

        unit_list.append(unit_options[unit_type - 1])       # appending the unit list as units are entered by the player

    return unit_list


def get_playa2_unit_list(num_players_playa2):           # passing the no. of players chosen by Player 2 as a parameter

    unit_list = []      # initializing an empty list

    playa2_money_left = num_players_playa2 - 1      # computing the money left for medics after Player 2's army creation
    print("\nWelcome, Player 2. Time to choose your army now. May the force be with you!")

    for i in range(num_players_playa2):     # looping over the number of players
        unit_type = -1
        incorrect_entered = False       # flag is set to false when valid number for unit is entered

        while unit_type < 1 or unit_type > 5:       # while the unit is between 1 and 5
            if incorrect_entered:
                print("Choose only valid inputs : 1, 2, 3, 4 or 5")     # error handling for invalid inputs

            unit_type = get_number_input(       # fetching the unit type from the player
                "Press 1 to add Soldier, 2 to add Knight, 3 to add an Archer, 4 to add Siege Equipment and 5 to add Wizard: ")

            incorrect_entered = True        # flag is set to true when an invalid input is given by the player

        print("Money left : " + str(playa2_money_left))     # printing the money left
        playa2_money_left = playa2_money_left - 1       # decrementing the money

        unit_list.append(unit_options[unit_type - 1])       # appending the unit list as units are entered by the player
    return unit_list


player1_set = get_playa1_unit_list(
    num_players_playa1)  # calling the input function of Player 1 to take n elements in the list

player2_set = get_playa2_unit_list(
    num_players_playa2)  # calling the input function of Player 2 to take n elements in the list

print("\nPlayer 1 chose the following units: ")

for unit in player1_set:
    print(unit.get_type())      # printing Player 1's units

print("\nPlayer 2 chose the following units: ")

for unit in player2_set:
    print(unit.get_type())      # printing Player 2's units

print("\n")
print(combat(player1_set, player2_set))     # passing the list of both players army