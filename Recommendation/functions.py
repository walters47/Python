from destinations import destinations_hash, destination

def suggest_attractions(destinations):
    attractions = []
    for destination in destinations.array:
        if destination:
            for item in destinations.retrieve(destination[0]).attractions:
                if item not in attractions:
                    attractions.append(item)
    print("Which of the following attractions appeal to you?: ")
    count = 1
    for item in attractions:
        print("{}. {}".format(count, item))
        count += 1
    return attractions

def retrieve_attractions(destinations):
    user_choices = []
    attractions = suggest_attractions(destinations)
    another_choice = True
    while another_choice and len(user_choices) <= 3:
        attraction = int(input("Please enter the number of the attraction that appeals to you: "))
        user_choices.append(attractions[attraction-1])
        ask_again = input("Would you like to make another selection? Yes/No: ").lower()
        if ask_again[0] == "n":
            another_choice = False
    return user_choices