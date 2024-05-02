def main():
    read_data()

    cart = Cart()
    
    while True:
        menu()
    
        try:
            choice = int(input("Choose an option by typing the number: "))
        except ValueError:
            print("Invalid input, please enter a number")
            continue
        
        if choice == 1:
            print("\nInventory:")
            for article in Inventory.values():
                print(article)
        
        elif choice == 2:
            try:
                name = input("Enter product name: ")
                quantity = int(input("Enter quantity: "))
                cart.addProduct(name, quantity)
            except ValueError:
                print("Invalid input, please try again")
        
        elif choice == 3:
            try:
                name = input("Enter product name: ")
                quantity = int(input("Enter quantity: "))
                cart.removeProduct(name, quantity)
            except ValueError:
                print("Invalid input, please try again")
        
        elif choice == 4:
            cart.displayCart()
        
        elif choice == 5:
            cart.checkout()
        
        elif choice == 6:
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please try again.")


if __name__=='__main__':
    main()