class Product:
    def __init__(self, name="", price=0.0, discountPercent=0):
            self.name = name
            self.price = price
            self.discountPercent = discountPercent

    def getDiscountAmount(self):
        return self.price * self.discountPercent / 100

    def getDiscountPrice(self):
        return self.price - self.getDiscountAmount()

    def getDescription(self):
        return self.name

#new class for Media
class Media(Product):
    def __init__(self, name="", price=0.0, discountPercent=0, format=""):
        Product.__init__(self, name, price, discountPercent)
        self.format = format
    
class Book(Media):
    def __init__(self, name="", price=0.0, discountPercent=0, author="", format='Hardcover'):#default format is Hardcover
        Media.__init__(self, name, price, discountPercent, format)
        self.author = author
        self.format = format

    def getDescription(self):
        return Media.getDescription(self) + " by " + self.author 
                
class Movie(Media):
    def __init__(self, name="", price=0.0, discountPercent=0, year=0, format="DVD"):#default format is DVD
        Media.__init__(self, name, price, discountPercent, format)
        self.year = year
        self.format = format

    def getDescription(self):
        return f'{Media.getDescription(self)} - ({self.year})'

#new class for Album
class Album(Media):
    def __init__(self, name="", price=0.0, discountPercent=0, artist="", format="MP3"):
        Media.__init__(self, name, price, discountPercent, format)
        self.artist = artist
        self.format = format
    
    def getDescription(self):
        return f'{Media.getDescription(self)} - ({self.artist})'

