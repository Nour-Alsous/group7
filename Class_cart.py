class Cart:
    def __init__(self):#constructor
        self.listofpurchased = []

    def addProduct(self, name, quantity):#function to add a product to a cart and specifying the necessary exceptions
        
            if name in Inventory:
                article = Inventory[name]
                quantity_available = article.getQuantity()
                
                if quantity > quantity_available:
                    quantity = quantity_available
                
                article.setQuantity(quantity_available - quantity)
                
                for purchased in self.listofpurchased:
                    if purchased.getName() == name:
                        purchased.setQuantity(purchased.getQuantity() + quantity)
                        return
                
                new_article = Article(name, article.getPrice(), quantity)
                self.listofpurchased.append(new_article)
            else:
                print("Product '" + name + "' not found in inventory.")

    def removeProduct(self, name, quantity):#fuction for removing an item from the cart
        
            for purchased in self.listofpurchased:
                if purchased.getName() == name:
                    if quantity >= purchased.getQuantity():
                        Inventory[name].setQuantity(Inventory[name].getQuantity() + purchased.getQuantity())
                        self.listofpurchased.remove(purchased)
                    else:
                        purchased.setQuantity(purchased.getQuantity() - quantity)
                        Inventory[name].setQuantity(Inventory[name].getQuantity() + quantity)
                    return



    def displayCart(self):#function to diplay the items in the cart
        if not self.listofpurchased:
            print("The cart is empty.")
        else:
            print("Cart Contents:")
            for i in self.listofpurchased:
                print(i)

    def checkout(self):#function to checkout
        
            total_bill = 0
            for i in self.listofpurchased:
                quantity = i.getQuantity()
                price = i.getPrice()
                
                if quantity >= 3:
                    price *= 0.9
                
                total_bill += quantity * price
            
            total_bill *= 1.07
            
            print("Total bill (including VAT): $", total_bill)