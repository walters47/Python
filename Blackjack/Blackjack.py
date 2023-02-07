import Blackjack_functions

cards = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "Jack": 10, "Queen": 10, "King": 10, "Ace": 11}


print("""
=========
Blackjack
=========
Welcome to Blackjack!
The object of the game is to hold cards as close in value as possible to 21, without going over.
If you beat the dealer, you double your bet!
All players begin with £100. The minimum bet is £5
""")
Blackjack_functions.player_add(Blackjack_functions.player_name)
while Blackjack_functions.player_1.at_the_table == True or Blackjack_functions.player_2.at_the_table == True or Blackjack_functions.player_3.at_the_table == True or Blackjack_functions.player_4.at_the_table == True or Blackjack_functions.player_5.at_the_table == True:
    Blackjack_functions.place_your_bets(Blackjack_functions.Player.player_count)
    Blackjack_functions.opening_hand(Blackjack_functions.Player.player_count)
    Blackjack_functions.player_turns(Blackjack_functions.Player.player_count)
    Blackjack_functions.dealer_turn()
    Blackjack_functions.end_of_round(Blackjack_functions.Player.player_count)
print("""
No players remain at the table.
The game is over, thanks for playing!
""")