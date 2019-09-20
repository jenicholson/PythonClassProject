import PlayerClass as yahtzee

name_1 = input("What is the name of Player 1? ")
player_1 = yahtzee.Player(name_1)

name_2 = input("\nWhat is the name of Player 2? ")
player_2 = yahtzee.Player(name_2)

input("Press enter to start\n...\n")

print("Rules to Play")

print("\nThe goal of the game is to get the highest point total possible. "
      "\nEach player will take turns rolling the dice. "
      "\nBased on the dice shown, choose the category that will maximize your score. "
      "\nOnes through Sixes will multiply the number in that category by the quantity of dice with that number. "
      "\nChance will total the sum of all the dice. "
      "\nThe game ends when each player fills all seven categories. "
      "\nA bonus of 35 points is added if a player ends with a total score of 63 or above. "
      "\nThe player with the highest point total wins the game!")

print("\n{}, {}, ready to play?".format(player_1.player_name, player_2.player_name))

input("\nPress enter to begin the game\n...\n")

turn = 1

my_categories=yahtzee.Categories()
my_colors=yahtzee.bcolors()

while len(player_1.remaining_categories) != 0 and len(player_2.remaining_categories) != 0:
    print(my_colors.bold + my_colors.blue)
    print("\nTurn {}".format(turn))

    print("\n{} start\n".format(player_1.player_name))

    press_enter=input("{}, press enter to roll\n...\n".format(player_1.player_name))

    dice_roll = player_1.roll_dice(5)

    player1_choice=player_1.choose_category(my_categories)

    player1_score=player_1.scoring(player1_choice, dice_roll)

    player_1.update_score_card(player1_choice, player1_score, my_categories)

    player_1.print_score_card(my_categories)

    player_1.update_score()

    # yahtzee.print_remaining_categories()
    print(my_colors.bold + my_colors.purple)
    print("\n{} start\n".format(player_2.player_name))

    press_enter=input("{}, press enter to roll\n...\n".format(player_2.player_name))

    dice_roll = player_2.roll_dice(5)

    player2_choice = player_2.choose_category(my_categories)

    player2_score = player_2.scoring(player2_choice, dice_roll)

    player_2.update_score_card(player2_choice, player2_score, my_categories)

    player_2.print_score_card(my_categories)

    player_2.update_score()

    turn += 1

print(my_colors.bold + my_colors.endc + "\nGAME OVER\n")

if player_1.get_score() >= 63:
    player_1.current_score = player_1.get_score()+35
    print(my_colors.bold + my_colors.green + "Congrats, {}! You got the bonus! Your score is now {}".format(player_1.player_name,player_1.get_score()))
else:
    print(my_colors.endc + "Sorry, {}! You didn't get the bonus this time.".format(player_1.player_name))

if player_2.get_score() >= 63:
    player_2.current_score = player_2.get_score() + 35
    print(my_colors.bold + my_colors.green + "Congrats, {}! You got the bonus! Your score is now {}\n".format(player_2.player_name,player_2.get_score()))
else:
    print(my_colors.endc + "Sorry, {}! You didn't get the bonus this time.\n".format(player_2.player_name))

print(my_colors.bold + my_colors.endc + "The final score for {} was {}".format(player_1.player_name, player_1.get_score()))
print(my_colors.bold + my_colors.endc + "The final score for {} was {}\n".format(player_2.player_name, player_2.get_score()))

if player_1.get_score() > player_2.get_score():
    print(my_colors.bold + my_colors.underline + my_colors.green + "***{} WINS!***".format(player_1.player_name))
elif player_2.get_score() > player_1.get_score():
    print(my_colors.bold + my_colors.underline + my_colors.green + "***{} WINS!***".format(player_2.player_name))
else:
    print(my_colors.endc + "{} and {} tied! Great job!".format(player_1.player_name, player_2.player_name))