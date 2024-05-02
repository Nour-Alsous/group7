class Article:
    def __init__(self, name, price, quantity):# using a constructor
        self.name = name
        self.price = price
        self.quantity = quantity
     
     #now defining getter functions and setter functions
    def getName(self): 
        return self.name

    def getPrice(self):
        return self.price

    def getQuantity(self):
        return self.quantity

    def setQuantity(self, newquantity):
        self.quantity = newquantity
    #using a special method str
    def __str__(self):
        return "Article: " + str(self.name) + ", Quantity: " + str(self.quantity) + ", Pri