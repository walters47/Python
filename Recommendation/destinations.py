from HashMap import HashMap

destinations_hash = HashMap(8)

class destination:
    def __init__(self, name, weather, cost, safety, food=[], attractions=[]):
        self.name = name
        self.weather = weather
        self.cost = cost
        self.food = food
        self.attractions = attractions
        self.safety = safety
        self.hashify()

    def hashify(self):
        destinations_hash.assign(self.name, self)

Korea = destination("Korea", "Seasonal", "Expensive", "High", ["Spicy", "Meat"], ["Historical Sites", "Culture"])
Maldives = destination("Maldives", "Sunny", "Expensive", "High", ["Fish", "Curry"], ["Beaches", "Natural Beauty"])
India = destination("India", "Sunny", "Cheap", "Low", ["Spicy", "Vegetarian", "Curry"], ["Historical Sites", "Natural Beauty", "Culture", "Wildlife"])
Australia = destination("Australia", "Sunny", "Expensive", "High", ["Meat", "Barbecue", "International"], ["Natural Beauty", "Beaches", "Wildlife", "Sport", "Nightlife"])
South_Africa = destination("South Africa", "Sunny", "Moderate", "Low", ["Meat", "Barbecue"], ["Natural Beauty", "Wildlife", "Sport", "Culture"])
Brazil = destination("Brazil", "Sunny", "Cheap", "Low", ["Meat", "Barbecue"], ["Natural Beauty", "Beaches", "Sport", "Culture"])
Iceland = destination("Iceland", "Cold", "Expensive", "High", ["Fish"], ["Natural Beauty"])
U_S_A = destination("USA", "Seasonal", "Expensive", "High", ["Meat", "Barbecue", "International"], ["Historical Sites", "Culture", "Natural Beauty", "Sport", "Nightlife"])