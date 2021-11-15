class Country:

    def __init__(self, name, city, population, currency, language, visited = False, id = None):
        self.name = name
        self.city = city
        self.population = population
        self.currency = currency
        self.language = language
        self.visited = visited
        self.id = id
        
    def check_visited(self):
        self.completed = True
