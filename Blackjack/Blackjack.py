cards = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "Jack": 10, "Queen": 10, "King": 10, "Ace": 11}

class Player():

    player_count = 1

    def __init__(self, new_name):
        self.name = new_name
        self.money = 100
        self.bet = 0
        self.hand = []
        self.card_value = 0
        self.is_bust = False
        Player.player_count += 1
    
dealer_hand = []
dealer_card_value = 0
dealer_is_bust = False
player_name = ""

def player_intro():
    input("Please, enter your name:")
    player_name = input
    return player_name

def player_init():
    if Player.player_count == 1:
        player_1 = Player(player_name)
    elif Player.player_name == 2:
        player_2 = Player(player_name)
    elif Player.player_name == 3:
        player_3 = Player(player_name)
    elif Player.player_name == 4:
        player_4 = Player(player_name)
    elif Player.player_name == 5:
        player_5 = Player(player_name)

def player_add():
    player_intro()
    player_init()
    while Player.player_count <= 5:
        input("Are there any additional players? Y/N:")
        if input.lower() == "y":
            player_intro()
            player_init()
        elif input.lower() == "n":
            print("Ok, let's play!")
        elif Player.player_count == 5:
            print("That's five, let's play!")
    


print("""
=========
Blackjack
=========
Welcome to Blackjack!
The object of the game is to hold cards as close in value as possible to 21, without going over.
If you beat the dealer, you double your bet!
""")
player_add()