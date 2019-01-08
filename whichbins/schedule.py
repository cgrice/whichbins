class Schedule:

    def __init__(self):
        self.schedule = {}

    def onDate(self, date):
        try:
            return self.schedule[date]
        except KeyError:
            return None

    def add(self, date, collection):
        defaultCollection = {
            "black": False,
            "blue": False,
            "brown": False,
            "green": False
        }
        # Merge the collection with the default to save having to 
        # pass all the non-collected bins
        self.schedule[date] = { **defaultCollection, **collection }