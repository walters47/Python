import random

cards = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "Jack": 10, "Queen": 10, "King": 10, "Ace": 11}

class Player():
    player_count = 1

    def __init__(self):
        self.name = ""
        self.money = 100
        self.bet = 0
        self.hand = []
        self.card_value = 0
        self.is_bust = False

    def __repr__(self):
        return self.name

    def place_bet(self):
        self.bet = int(input("{}, you have £{} remaining. How much would you like to bet? £".format(self, self.money)))
        while self.bet not in range(5, self.money + 1):
            self.bet = int(input("Invalid bet. Please enter a value between £5 and £{}: £".format(self.money)))
        print("{} has bet £{}.".format(self.name, self.bet))

    def name_player(self, player_name):
        player_name = input("Please enter your name: ")
        self.name = player_name
        print("Welcome, " + self.name)
        Player.player_count += 1

    def deal_card(self):
        random_card = random.choice(list(cards.keys()))
        self.hand.append(random_card)
        self.card_value += cards[random_card]
        print("{}: {}".format(self.name, self.hand))
        print("Your total is {}".format(self.card_value))
    
    #def __del__(self):
        #print(self.name + " has left the table")
       # Player.player_count -= 1
  
dealer_hand = []
dealer_card_value = 0
dealer_is_bust = False
player_1 = Player()
player_2 = Player()
player_3 = Player()
player_4 = Player()
player_5 = Player()
player_name = ""

def player_init(player_name):
    if Player.player_count == 1:
        player_1.name_player(player_name)
    elif Player.player_count == 2:
        player_2.name_player(player_name)
    elif Player.player_count == 3:
        player_3.name_player(player_name)
    elif Player.player_count == 4:
        player_4.name_player(player_name)
    elif Player.player_count == 5:
        player_5.name_player(player_name)
    return player_1, player_2, player_3, player_4, player_5
    
def player_add(player_name):
    player_init(player_name)
    while Player.player_count <= 5:
        y_or_n = input("Are there any additional players? Y/N: ")
        if y_or_n.lower() == "y":
            player_init(player_name)
        elif y_or_n.lower() == "n":
            print("Ok, let's play!")
            break
    if Player.player_count == 6:
        print("That's five, let's play!")
    return player_1, player_2, player_3, player_4, player_5

def place_your_bets(no_of_players):
    print("All players begin with £100. The minimum bet is £5")
    player_1.place_bet()
    if no_of_players > 2:
        player_2.place_bet()
    if no_of_players > 3:
        player_3.place_bet()
    if no_of_players > 4:
        player_4.place_bet()
    if no_of_players > 5:
        player_5.place_bet()

def deal_to_dealer(dealer_card_value):
    random_card = random.choice(list(cards.keys()))
    dealer_hand.append(random_card)
    dealer_card_value += cards[random_card]
    if len(dealer_hand) == 2:
        print("Dealer's 2nd card: {}".format(dealer_hand[1]))

def deal_cards(no_of_players):
    print("Dealing cards to all players:")
    player_1.deal_card()
    if no_of_players > 2:
        player_2.deal_card()
    if no_of_players > 3:
        player_3.deal_card()
    if no_of_players > 4:
        player_4.deal_card()
    if no_of_players > 5:
        player_5.deal_card()
    deal_to_dealer(dealer_card_value)
    
print("""
=========
Blackjack
=========
Welcome to Blackjack!
The object of the game is to hold cards as close in value as possible to 21, without going over.
If you beat the dealer, you double your bet!
""")
player_add(player_name)
place_your_bets(Player.player_count)
deal_cards(Player.player_count)
deal_cards(Player.player_count)
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