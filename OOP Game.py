class Fighter:

    def __init__(self, fighter_name, fighter_country, fighter_attack, fighter_defense, fighter_hitpoints):
        self.name = fighter_name
        self.country = fighter_country
        self.attack = fighter_attack
        self.defense = fighter_defense
        self.hp = fighter_hitpoints
        self.k_o = False
        self.is_attacking = False
        self.is_defending = False
        self.is_counterattacking = False

    def __repr__(self):
        print("{} is a fighter from {}. They have {} hit points, an attack rating of {} and a defense rating of {}".format(self.name, self.country, str(self.hp), str(self.attack), str(self.defense)))

    def k_o(self, opponent):
        if self.hp == 0:
            self.k_o = True
            print("{} was knocked out! {} wins!".format(self.name, opponent))

    def opening_stance(self):
        stance = input("""
        {}, choose your opening stance:
        1. Attack
        2. Defense
        3. Counterattack
        """.format(self.name))
        while stance != 1 or 2 or 3:
            stance = input("Please enter the number 1, 2 or 3: ")
        if stance == 1:
            self.is_attacking = True
        elif stance == 2:
            self.is_defending = True
        else:
            self.is_counterattacking = True
    
    def use_attack(self, opponent_def, opponent_hp):
        self.is_attacking = True
        
