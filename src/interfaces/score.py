class Score:
    def __init__(self, duration=None):

        # Default variables
        if duration==None: self.duration = 10

        self.duration = duration
        self.hits = 0
        self.misses = 0

    def hit(self):
        self.hits += 1
    
    def miss(self):
        self.misses += 1
    
    def calculate(self):
        return self.hits*1000 - self.misses*10