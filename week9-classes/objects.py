class Movie:
    # contructor that accepts a name and a year
    def __init__(self, name, year):
        self.name = name
        self.year = year

    # getStr method returns movie name with year in (parens)
    def getStr(self):
        return f'{self.name} ({self.year})'