import random
import Blackjack_functions

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
                print("{} has gone bust! They lose their bet. You have £{} remaining".format(self.name, self.money))
            elif self.card_value == 21 and len(self.hand) == 2:
                self.has_won = True
                self.money += self.bet
                print("{} has Blackjack! Congratulations, you win! You now have £{}".format(self.name, self.money))
            elif self.card_value == 21:
                self.has_stuck = True
                print("{}, that's 21! If the dealer does not finish with 21, you will win!".format(self.name))
    
    def player_turn(self):
        while self.is_bust == False and self.has_won == False and self.has_stuck == False and self.at_the_table == True:
            hit_or_stick = input("{}, your total is {}. Do you want to hit or stick? H/S: ".format(self.name, self.card_value))
            if hit_or_stick.lower() == "h":
                self.deal_card()
                self.blackjack_or_bust()
            elif hit_or_stick.lower() == "s":
                self.has_stuck = True
        
    def beat_the_dealer(self):
        if self.has_stuck == True:
            if self.card_value > Blackjack_functions.dealer_card_value:
                if Blackjack_functions.dealer_has_stuck == True or Blackjack_functions.dealer_is_bust == True:
                    self.has_won = True
                    self.money += self.bet
                    print("{}, your score of {} has beat the dealer! Congratulations! You now have £{}".format(self.name, self.card_value, self.money))
            elif self.card_value <= Blackjack_functions.dealer_card_value:
                if Blackjack_functions.dealer_has_stuck == True and Blackjack_functions.dealer_is_bust == False:
                    self.money -= self.bet
                    print("{}, your score of {} failed to beat the dealer! You lose your bet. You now have £{} remaining.".format(self.name, self.card_value, self.money))
    
    
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
                print("You do not have enough money to make the minimum bet. {} is now out of the game.".format(self.name))
                self.money = 0
                self.reset_player()
                self.at_the_table = False
            else:
                cash_out = input("Do you want to cash out? Y/N: ")
                if cash_out.lower() == "y":
                    print("{} has cashed out and left the table.".format(self.name))
                    self.money = 0
                    self.reset_player()
                    self.at_the_table = False
                else:
                    print("Okay, let's play another hand!")
                    self.reset_player()
                    
