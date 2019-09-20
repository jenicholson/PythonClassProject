from random import randint

__author__ = 'Awesome Yahtzee Players'

"""This code defines the class of players for our Yahtzee game."""
class bcolors:
    def __init__(self):
        self.purple = '\033[95m'
        self.red = '\033[91m'
        self.endc = '\033[0m'
        self.bold = '\033[1m'
        self.underline = '\033[4m'
        self.blue = '\033[34m'
        self.green = '\033[32m'

class Categories:
    def __init__(self):
        self.categories = {1:"ones", 2:"twos", 3:"threes", 4:"fours", 5:"fives", 6:"sixes", 7:"chance"}

    def get_categories(self):
        return self.categories

class Player:
    def __init__(self, player_name):
        self.player_name = player_name
        self.scorecard = {"ones": 0,
                          "twos": 0,
                          "threes": 0,
                          "fours": 0,
                          "fives": 0,
                          "sixes": 0,
                          "chance": 0}
        self.remaining_categories = {1:"ones", 2:"twos", 3:"threes", 4:"fours", 5:"fives", 6:"sixes", 7:"chance"}
        self.current_score=0

    def roll_dice(self, number_to_roll):
        """User enters the number of dice to roll and the function returns
        a list with 'number_to_roll' number of random numbers"""
        dice = []
        for i in range(0, number_to_roll):
            dice.append(randint(1, 6))
        print("The dice you rolled are {}.\n".format(dice))
        return dice

    def choose_category(self, categories):
        """This chooses the category for your dice roll"""
        print("Your available categories are:\n")
        for option in self.remaining_categories:
            print(option, self.remaining_categories[option])

        select_category = int(input("\nSelect a numeric category to assign your roll: "))
        while select_category not in self.remaining_categories:
            select_category = int(input("Category unavailable. Select a numeric category to assign your roll: "))
        print("\nYou selected", categories.get_categories()[select_category])
        self.remaining_categories.pop(select_category)
        # self.remaining_categories=categories.get_categories()
        # print(categories.get_categories())
        # print(self.remaining_categories)
        # print("\nRemaining categories are :")
        # for option in self.remaining_categories:
        #     print(option, self.remaining_categories[option])

        return select_category

    def scoring(self, select_category, dice):
        """This takes the category the player selected and creates the score"""
        if select_category<7:
            score=select_category*dice.count(select_category)
        else:
            score=sum(dice)
        print("Your score for this turn is: {}.".format(score))
        return score

    def update_score_card(self, chosen_category, scoring_result, my_categories):
        """This method takes the chosen_category from the choose_category method and the
        scoring_result from the scoring() and my_categories is an instance of the categories class
        # then uses them to update the player's scorecard"""
        self.scorecard[my_categories.get_categories()[chosen_category]] = int(scoring_result)
        # self.scorecard[my_categories.get_categories()[chosen_category]] = 4
        # print(scoring_result)

    def update_score(self):
        """This function takes the updated scorecard and updates the score."""
        tally = 0
        for ii in self.scorecard:
            tally = tally + self.scorecard[ii]
        self.current_score = tally

    def print_score(self):
        print(self.current_score)

    def get_score(self):
        return self.current_score

    def print_score_card(self,my_categories):
        """A very simple print out of the players score card."""
        # print(self.scorecard)
        print("1: {}\n2: {}\n3: {}\n4: {}\n5: {}\n6: {}\nChance: {}".format(self.scorecard[my_categories.get_categories()[1]],
                                                                            self.scorecard[my_categories.get_categories()[2]],
                                                                            self.scorecard[my_categories.get_categories()[3]],
                                                                            self.scorecard[my_categories.get_categories()[4]],
                                                                            self.scorecard[my_categories.get_categories()[5]],
                                                                            self.scorecard[my_categories.get_categories()[6]],
                                                                            self.scorecard[my_categories.get_categories()[7]]))

    def print_remaining_categories(self):
        print(self.remaining_categories)

# my_categories=Categories()
# Jessica = Player("Jessica")
# dice_roll1=Jessica.roll_dice(5)
# y=Jessica.choose_category(my_categories)
# x=Jessica.scoring(select_category=y, dice=dice_roll1)
# print(dice_roll1,x)
# Jessica.update_score_card(int(y), int(x), my_categories)
# Jessica.print_score_card()k
# Jessica.update_score()
# Jessica.print_score()
# # print(type(x))
# # print(type(y))
# # print(Jessica.score_card())

#class ComputerPlayer(Player):
#    """This class is a placeholder for a future computer player"""
#    def __init__(self):
#        self.player_name = "Evil Computer"
#        self.scorecard = {"ones": 0,
#                          "twos": 0,
#                          "threes": 0,
#                          "fours": 0,
#                          "fives": 0,
#                          "sixes": 0,
#                          "chance": 0}
#        self.remaining_categories = ["ones", "twos", "threes", "fours", "fives", "sixes", "chance"]
        
#Bill = ComputerPlayer()
#Bill.print_score_card()