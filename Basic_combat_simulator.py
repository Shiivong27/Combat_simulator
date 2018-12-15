class Unit:                      # a class unit defined to return the 'type' of the unit
  def __init__(self, type):      # which is passed to the who_wins function to determine the winner
    self.__type__ = type
  def get_type(self):
    return self.__type__


knight = Unit("knight")     # creating class objects for each of the units
archer = Unit("archer")
soldier = Unit("soldier")

print("Welcome, Commaders! Time to make your army.")

print("\nEach player has $10 each to make an army of 10 units which cost $1 each.\n")

unit_options = [soldier, knight, archer]        # a list of units for the players to choose from

def who_wins(unit1, unit2):     # all the game rules defined in one function

  if unit1.get_type() == unit2.get_type():
    return 'tie'

  elif unit1.get_type() == 'archer' and unit2.get_type() == 'soldier':
    return 'archer'

  elif unit1.get_type() == 'archer' and unit2.get_type() == 'knight':
    return 'knight'

  elif unit1.get_type() == 'knight' and unit2.get_type() == 'archer':
    return 'knight'

  elif unit1.get_type() == 'knight' and unit2.get_type() == 'soldier':
    return 'soldier'

  elif unit1.get_type() == 'soldier' and unit2.get_type() == 'knight':
    return 'soldier'

  elif unit1.get_type() == 'soldier' and unit2.get_type() == 'archer':
    return 'archer'



def combat(playa1, playa2):     # this function decides and displays the winner of each round

    score_playa1 = 0        # initializing player scores as zero
    score_playa2 = 0

    print("COMBAT RESULTS FOR ALL ROUNDS")      # just for a better display :)
    print("****** ******* *** *** ******")

    for index in range(len(playa1)):        # loop till all the 10 units of each players are exhausted
      unit1 = playa1[index]     # a variable which holds the unit information
      unit2 = playa2[index]     # for each player's list

      if who_wins(unit1, unit2) == unit1.get_type():        # fetching the results of the combat and declaring the round winner
        print("Player 1's " + unit1.get_type() + " wins against Player 2's " + unit2.get_type() + "!")
        score_playa1 += 1       # incrementing player score

      elif who_wins(unit1, unit2) == unit2.get_type():
        print("Player 2's " + unit2.get_type() + " wins against Player 1's " + unit1.get_type() + "!")
        score_playa2 += 1       # incrementing player score

      else:
        print("tie")        # in case of a tie
        continue        # giving back control to the loop

    if   score_playa1 > score_playa2:       # comparing the final scores of both players
                                            # and displaying the result
         print("\nPlayer 1 Wins!")

    elif score_playa2 > score_playa1:

         print("\nPlayer 2 Wins!")

    else: print("\nOh boy it's a Tie!!")
    print("\nPlayer 1 final score: " +  str(score_playa1) + "\n" + "\nPlayer 2 final score: " + str(score_playa2))


def get_playa1_unit_list(num_players):

    unit_list = []      # initializing an empty list

    playa1_money_left = 9       # player 1 money left

    print("Welcome, Player 1. Time to choose your army now. May the force be with you!")

    for i in range(num_players):        # looping over the number of units
        unit_type = -1
        incorrect_entered = False       # flag is set to false when valid number for unit is entered

        while unit_type < 1 or unit_type > 3:       # while the unit is between 1 and 3
            if incorrect_entered:
                print("Choose only valid inputs : 1, 2 or 3")       # error handling for invalid inputs
            unit_type = int(input("\nPress 1 to add Soldier, 2 to add Knight and 3 to add an Archer: "))
            incorrect_entered = True
        print("Money left: " + str(playa1_money_left))
        playa1_money_left -= 1      # decrementing the money


        unit_list.append(unit_options[unit_type - 1])       # appending the unit list as units are entered by the player

    return unit_list

def get_playa2_unit_list(num_players):

    unit_list = []      # initializing an empty list

    playa2_money_left = 9       # player 2 money left

    print("\nWelcome, Player 2. Time to choose your army now. May the force be with you!")


    for i in range(num_players):        # looping over the number of units
        unit_type = -1
        incorrect_entered = False       # flag is set to false when valid number for unit is entered

        while unit_type < 1 or unit_type > 3:       # while the unit is between 1 and 3
            if incorrect_entered:
                print("Choose only valid inputs : 1, 2 or 3")       # error handling for invalid inputs
            unit_type = int(input("Press 1 to add Soldier, 2 to add Knight and 3 to add an Archer: "))
            incorrect_entered = True
        print("Money left: " + str(playa2_money_left))
        playa2_money_left -= 1      # decrementing the money


        unit_list.append(unit_options[unit_type - 1])       # appending the unit list as units are entered by the player

    return unit_list

player1_set = get_playa1_unit_list(10)      # calling the input function of Player 1 to take 10 elements in the list

player2_set = get_playa2_unit_list(10)      # calling the input funciton of Player 2 to take 10 elements in the list

print("\nPlayer 1 chose the following units: ")

for unit in player1_set:        # displaying the units chosen by player 1
    print(unit.get_type())

print("\nPlayer 2 chose the following units: ")

for unit in player2_set:        # dislplaying the units chosen by player 2
    print(unit.get_type())

print("\n")
print(combat(player1_set, player2_set))     # calling the combat function to make the units fight in order