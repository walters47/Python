from HashMap import HashMap

destinations_hash = HashMap(10)

class destination:
    def __init__(self, name, weather, cost, safety, food=[], attractions=[]):
        self.name = name
        self.weather = weather
        self.cost = cost
        self.food = food
        self.attractions = attractions
        self.safety = safety

    def hashify(self):
        destinations_hash.assign(self.name, self)

Korea = destination("Korea", "Seasonal", "Expensive", "Safe", ["Spicy", "Meat"], ["Historical Sites", "Culture"])
Korea.hashify()
Maldives = destination("Maldives", "Sunny", "Expensive", "Safe", ["Fish", "Curry"], ["Beaches", "Natural Beauty"])
Maldives.hashify()