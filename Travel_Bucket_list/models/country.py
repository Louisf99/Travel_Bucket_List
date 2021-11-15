class Country:

    def __init__(self, name, population, currency, language, visited = False, id = None):
        self.name = name
        self.population = population
        self.currency = currency
        self.language = language
        self.visited = visited
        self.id = id
        self.cities = []

