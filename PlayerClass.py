__author__ = 'Awesome Yahtzee Players'

"""This code defines the class of players for our Yahtzee game."""

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
        self.remaining_categories = ["ones", "twos", "threes", "fours", "fives", "sixes", "chance"]
    
    def roll_dice():
        pass
    
    def choose_category():
        pass
    
    def update_remaining_categories():
        pass
    
    def scoring():
        pass
    
    def update_score_card():
        pass
    
    def tally_score():
        pass
    
    def print_score_card(self):
        """A very simple print out of the players score card."""
        print(self.scorecard)
        
    def print_remaining_categories(self):
        print(self.remaining_categories)
    
#Jessica = Player("Jessica")
#Jessica.print_score_card()
#Jessica.print_remaining_categories()
        
class ComputerPlayer(Player):
    """This class is a placeholder for a future computer player"""
    def __init__(self):
        self.player_name = "Evil Computer"
        self.scorecard = {"ones": 0,
                          "twos": 0,
                          "threes": 0,
                          "fours": 0,
                          "fives": 0,
                          "sixes": 0,
                          "chance": 0}
        self.remaining_categories = ["ones", "twos", "threes", "fours", "fives", "sixes", "chance"]
        
#Bill = ComputerPlayer()
#Bill.print_score_card()

