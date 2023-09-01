from destinations import destinations_hash, destination

def suggest_attractions():
    attractions = []
    for destination in destinations_hash.array:
        if destination:
            for item in destinations_hash.retrieve(destination[0]).attractions:
                if item not in attractions:
                    attractions.append(item)
    print("Which of the following attractions appeal to you?: ")
    count = 1
    for item in attractions:
        print("{}. {}".format(count, item))
        count += 1

suggest_attractions()