class Horse:
    def __init__(self, name, rider):
        self.name = name
        self.rider = rider

class Rider:
    def __init__(self, name):
        self.name = name

r = Rider('Take')
h = Horse('Kiseki', r)
print(h.rider.name)
