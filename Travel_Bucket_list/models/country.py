class Country:

    def __init__(self, name, user, population, city, currency, language, visited = False, id = None):
        self.name = name
        self.user = user
        self.population = population
        self.city = city
        self.currency = currency
        self.language = language
        self.visited = visited
        self.id = id
        
        
    def check_visited(self):
        self.completed = True
