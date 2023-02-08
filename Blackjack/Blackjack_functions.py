import random
from player import Player

cards = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "Jack": 10, "Queen": 10, "King": 10, "Ace": 11}
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
    global dealer_card_value
    global dealer_hand
    print("Dealer reveals their hand: {}".format(dealer_hand))
    print("Dealer total: {}".format(dealer_card_value))
    while dealer_has_stuck == False and dealer_is_bust == False:
        if dealer_card_value > 21 and "Ace" in dealer_hand:
            ace_index = dealer_hand.index("Ace")
            dealer_hand[ace_index] =  "Ace (1)"
            print("The dealer's Ace is now worth 1 to prevent them from going bust!")
            dealer_card_value -= 10
        elif dealer_card_value > 21:
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
    return dealer_has_stuck, dealer_is_bust, dealer_card_value, dealer_hand
    

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
    global dealer_hand
    global dealer_card_value
    global dealer_is_bust
    global dealer_has_stuck
    player_1.end_of_round()
    if no_of_players > 2:
        player_2.end_of_round()
    if no_of_players > 3:
        player_3.end_of_round()
    if no_of_players > 4:
        player_4.end_of_round()
    if no_of_players > 5:
        player_5.end_of_round()
    dealer_hand = []
    dealer_card_value = 0
    dealer_is_bust = False
    dealer_has_stuck = False
    return dealer_hand, dealer_card_value, dealer_is_bust, dealer_has_stuck