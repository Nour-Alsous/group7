AED_TO_EUR = 0.225
AED_TO_GBP = 0.209
AED_TO_USD = 0.272
EUR_TO_AED = 4.441
GBP_TO_AED = 4.789
USD_TO_AED = 3.668

def aed_to_eur(money):
    return money * AED_TO_EUR

def aed_to_gbp(money):
    return money * AED_TO_GBP

def aed_to_usd(money):
    return money * AED_TO_US
    
def usd_to_aed(amount):
    return amount * USD_TO_AED

def gbp_to_aed(amount):
    return amount * GBP_TO_AED

def eur_to_aed(amount):
    return amount * EUR_TO_AED

def main():
    print("Welcome to the currency converter!")
    while True:
        print("\nselect which currency you want to convert: ")
        print("1. AED to oother currencies")
        print("2. Other currencies to AED")
        print("3. Exit")

        choice = int(input("Enter your choice: "))
        if choice == 1:
            print("\n select the currency to convert from AED:")
            print("1. Euro (EUR)")
            print("2. British Pound (GBP)")
            print("3. US Dollar (USD) ")
            
            currency_choice=int(input("Enter your choice: "))
            if choice == 1:
                money = float(input("Enter the amount in AED: "))
                converted_amount = aed_to_eur(money)
                print(f"{money} AED is equal to {converted_amount} EUR")
            elif currency_choice == 2:
                money = float(input("Enter the amount in AED: "))
                converted_amount = aed_to_gbp(money)
                print(f"{money} AED is equal to {converted_amount} GBP")
            elif currency_choice == 3:
                money = float(input("Enter the amount in AED: "))
                converted_amount = aed_to_usd(money)
                print(f"{money} AED is equal to {converted_amount} USD")
            else: 
                print("Invalid choice! Try again!")
        elif choice == 2:
            print("\nSelect the currency to convert to AED")
            print("1. Euro (EUR)")
            print("2. British Pound (GBP)")
            print("3. US Dollar (USD)")

            currency_choice = int(input("Enter your choice: "))
            if currency_choice == 1:
                amount = float(input("Enter the amount in EUR: "))
                converted_amount = eur_to_aed(amount)
                print(f"{amount} EUR is equal to {converted_amount} AED")
            elif currency_choice == 2:
                amount = float(input("Enter the amount in GBP: "))
                converted_amount = gbp_to_aed(amount)
                print(f"{amount} GBP is equal to {converted_amount} AED")
            elif currency_choice == 3:
                amount = float(input("Enter the amount in USD: "))
                converted_amount = usd_to_aed(amount)
                print(f"{amount} USD is equal to {converted_amount} AED")
            else:
                print("Invalid choice! Try again!")
        elif choice == 3:
            print("Goodbye! I hope you have a great day!")
            break
        else: 
            print("invalid choice! Try again!")

if __name__ == "__main__":
    main()
    