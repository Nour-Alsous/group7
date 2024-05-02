def read_data():
    try:
        with open('products.csv') as file:
            n = csv.reader(file)
            next(n)
            for row in n:
                try:
                    name, price, quantity = row
                    price = float(price)
                    quantity = int(quantity)
                    Inventory[name] = Article(name, price, quantity)
                except ValueError:
                    print("Skipping invalid row:", row)
    except FileNotFoundError:
        print("Error: 'products.csv' file not found.")
    except Exception as e:
        print("An error occurred while reading data:", e)
    