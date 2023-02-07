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
        self.has_won = False
        self.has_stuck = False
        self.at_the_table = False

    def __repr__(self):
        return self.name

    def place_bet(self):
        if self.at_the_table == True:
            self.bet = int(input("{}, you have £{} remaining. How much would you like to bet? £".format(self, self.money)))
            while self.bet not in range(5, self.money + 1):
                self.bet = int(input("Invalid bet. Please enter a value between £5 and £{}: £".format(self.money)))
            print("{} has bet £{}.".format(self.name, self.bet))

    def name_player(self, player_name):
        player_name = input("Please enter your name: ")
        self.name = player_name
        print("Welcome, " + self.name)
        Player.player_count += 1
        self.at_the_table = True

    def deal_card(self):
        if self.at_the_table == True:
            random_card = random.choice(list(cards.keys()))
            self.hand.append(random_card)
            self.card_value += cards[random_card]
            print("{}: {}".format(self.name, self.hand))
            print("Your total is {}".format(self.card_value))

    def blackjack_or_bust(self):
        if self.at_the_table == True:
            if self.card_value > 21 and "Ace" in self.hand:
                ace_index = self.hand.index("Ace")
                self.hand[ace_index] =  "Ace (1)"
                print("Your Ace is now worth 1 to prevent you from going bust!")
                self.card_value -= 10
            elif self.card_value > 21:
                self.is_bust = True
                self.money -= self.bet
                print("{} has gone bust! They lose their bet.".format(self.name))
            elif self.card_value == 21 and len(self.hand) == 2:
                self.has_won = True
                self.money += self.bet
                print("{} has Blackjack! Congratulations, you win!".format(self.name))
            elif self.card_value == 21:
                self.has_stuck = True
                print("{}, that's 21! If the dealer does not finish with 21, you will win!".format(self.name))
            
    def beat_the_dealer(self):
        if self.has_stuck == True:
            if self.card_value > dealer_card_value:
                if dealer_has_stuck == True or dealer_is_bust == True:
                    self.has_won = True
                    self.money += self.bet
                    print("{}, your score of {} has beat the dealer! Congratulations!".format(self.name, self.card_value))
            elif self.card_value <= dealer_card_value:
                if dealer_has_stuck == True and dealer_is_bust == False:
                    self.money -= self.bet
                    print("{}, your score of {} failed to beat the dealer! You lose your bet.".format(self.name, self.card_value))
    
    def player_turn(self):
        while self.is_bust == False and self.has_won == False and self.has_stuck == False and self.at_the_table == True:
            hit_or_stick = input("{}, your total is {}. Do you want to hit or stick? H/S: ".format(self.name, self.card_value))
            if hit_or_stick.lower() == "h":
                self.deal_card()
                self.blackjack_or_bust()
            elif hit_or_stick.lower() == "s":
                self.has_stuck = True

    def reset_player(self):
        self.bet = 0
        self.hand = []
        self.card_value = 0
        self.is_bust = False
        self.has_won = False
        self.has_stuck = False
    
    def end_of_round(self):
        if self.at_the_table == True:
            print("{}, you have £{} remaining.".format(self.name, self.money))
            if self.money < 5:
                print("You do not have enough money to make the minimum bet. You are now out of the game.")
                self.money = 0
                self.reset_player()
                self.at_the_table = False
            else:
                cash_out = input("Do you want to cash out? Y/N: ")
                if cash_out.lower() == "y":
                    print("You have cashed out and left the table.")
                    self.money = 0
                    self.reset_player()
                    self.at_the_table = False
                else:
                    print("Okay, let's play another hand!")
                    self.reset_player()

dealer_hand = []
dealer_card_value = 0
dealer_is_bust = False
dealer_has_stuck = False
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

def deal_to_dealer():
    global dealer_card_value
    random_card = random.choice(list(cards.keys()))
    dealer_hand.append(random_card)
    dealer_card_value += cards[random_card]
    return dealer_card_value

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
    deal_to_dealer()
    print("Dealer's 1st card: {}".format(dealer_hand[0]))
    return dealer_card_value

def opening_hand(no_of_players):
    deal_cards(no_of_players)
    deal_cards(no_of_players)
    player_1.blackjack_or_bust()
    if no_of_players > 2:
        player_2.blackjack_or_bust()
    if no_of_players > 3:
        player_3.blackjack_or_bust()
    if no_of_players > 4:
        player_4.blackjack_or_bust()
    if no_of_players > 5:
        player_5.blackjack_or_bust()

def dealer_turn():
    global dealer_has_stuck
    global dealer_is_bust
    print("Dealer reveals their hand: {}".format(dealer_hand))
    print("Dealer total: {}".format(dealer_card_value))
    while dealer_has_stuck == False and dealer_is_bust == False:
        if dealer_card_value > 21:
            dealer_is_bust = True
            print("The dealer has gone bust!")
            break
        elif dealer_card_value in range(17, 22):
            dealer_has_stuck = True
            print("The dealer sticks on {}".format(dealer_card_value))
            break
        elif dealer_card_value < 17:
            deal_to_dealer()
            print("Dealer hand: {}".format(dealer_hand))
            print("Dealer total: {}".format(dealer_card_value))
    check_vs_dealer(Player.player_count)
    return dealer_has_stuck, dealer_is_bust, dealer_card_value
    

def player_turns(no_of_players):
    player_1.player_turn()
    if no_of_players > 2:
        player_2.player_turn()
    if no_of_players > 3:
        player_3.player_turn()
    if no_of_players > 4:
        player_4.player_turn()
    if no_of_players > 5:
        player_5.player_turn()

def check_vs_dealer(no_of_players):
    player_1.beat_the_dealer()
    if no_of_players > 2:
        player_2.beat_the_dealer()
    if no_of_players > 3:
        player_3.beat_the_dealer()
    if no_of_players > 4:
        player_4.beat_the_dealer()
    if no_of_players > 5:
        player_5.beat_the_dealer()

def end_of_round(no_of_players):
    player_1.end_of_round()
    if no_of_players > 2:
        player_2.end_of_round()
    if no_of_players > 3:
        player_3.end_of_round()
    if no_of_players > 4:
        player_4.end_of_round()
    if no_of_players > 5:
        player_5.end_of_round()

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
opening_hand(Player.player_count)
player_turns(Player.player_count)
dealer_turn()
end_of_round(Player.player_count)
#Check players vs dealer
#Declare winners/losers and tell current funds
#If money == 0, give the stanky boot
#Offer opportunity to leave table
#If 0 players remain, end the game