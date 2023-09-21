from destinations import destinations_hash, destination
from HashMap import HashMap

def recommendation(destinations_hash):
    user_destinations = destinations_hash.array
    print("Time to find you your ideal holiday destination!")
    user_destinations = destinations_from_weather(user_destinations)
    user_destinations = destinations_from_price(user_destinations)
    user_destinations = destinations_from_attractions(user_destinations)


def destinations_from_weather(destinations):
    user_destinations = []
    user_weather_pref = input("Your options for weather are: Sunny, Cold, Seasonal or Any.\nPlease enter your preference: ").lower()
    if user_weather_pref == "any":
        print("Your possible destinations are: \n")
        for destination in destinations:
            print(destination[0])
        return destinations
    else:
        for destination in destinations:
            if destination[1].weather.lower() == user_weather_pref:
                user_destinations.append(destination)
        print("Your possible destinations are:")
        for destination in user_destinations:
            print(destination[0])
        return user_destinations
    
def destinations_from_price(destinations):
    user_destinations = []
    user_weather_pref = input("Your options for cost are: Cheap, Moderate, Expensive or Any.\nPlease enter your preference: ").lower()
    if user_weather_pref == "any" or "expensive":
        print("Your possible destinations are: \n")
        for destination in destinations:
            print(destination[0])
        return destinations
    elif user_weather_pref == "moderate":
        for destination in destinations:
            if destination[1].cost.lower() == "moderate" or "cheap":
                user_destinations.append(destination)
        print("Your possible destinations are:")
        for destination in user_destinations:
            print(destination[0])
        return user_destinations
    else:
        for destination in destinations:
            if destination[1].cost.lower() == "cheap":
                user_destinations.append(destination)
        print("Your possible destinations are:")
        for destination in user_destinations:
            print(destination[0])
        return user_destinations


def suggest_attractions(destinations):
    attractions = []
    for destination in destinations:
        if destination:
            for item in destination[1].attractions:
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
    while len(user_choices) < 3:
        attraction = int(input("Please enter the number of the attraction that appeals to you: "))
        user_choices.append(attractions[attraction-1])
        ask_again = input("Would you like to make another selection? Yes/No: ").lower()
        if ask_again[0] == "n":
            break
    return user_choices

def destinations_from_attractions(destinations):
    user_destinations = []
    user_choices = retrieve_attractions(destinations)
    for destination in destinations:
        for item in destination[1].attractions:
            if item in user_choices:
                if destination not in user_destinations:
                    user_destinations.append(destination)
    print("Your possible destinations are:")
    for destination in user_destinations:
        print(destination[0])
    return user_destinations

#recommendation(destinations_hash)