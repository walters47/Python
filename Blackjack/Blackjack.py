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
    player_name = input("Please enter your name: ")
    print("Welcome, " + player_name)
    return player_name

def player_init():
    if Player.player_count == 1:
        player_1 = Player(player_name)
    elif Player.player_count == 2:
        player_2 = Player(player_name)
    elif Player.player_count == 3:
        player_3 = Player(player_name)
    elif Player.player_count == 4:
        player_4 = Player(player_name)
    elif Player.player_count == 5:
        player_5 = Player(player_name)

def player_add():
    player_intro()
    player_init()
    while Player.player_count <= 5:
        y_or_n = input("Are there any additional players? Y/N: ")
        if y_or_n.lower() == "y":
            player_intro()
            player_init()
        elif y_or_n.lower() == "n":
            print("Ok, let's play!")
            break
    if Player.player_count == 6:
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
#Players place bets
#Deal 1 card to each player 'face up', 1 to dealer 'face down'
#Deal 2nd card to all 'face up'
#Check for bust/blackjack
#Cycle through player turns
#Dealer turn
#Check players vs dealer
#Declare winners/losers and tell current funds
#If money == 0, give the stanky boot
#Offer opportunity to leave table
#If 0 players remain, end the game