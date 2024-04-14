def stage3(column):
    while True:
        try:
            sort_option = int(input("Choose sorting option:\n"
                                    "1. Ascending order\n"
                                    "2. Descending order\n"
                                    "Enter your choice: "))
            if sort_option == 1:
                sorted_column = sorted(column)
            elif sort_option == 2:
                sorted_column = sorted(column, reverse=True)
            else:
                print("Invalid choice! Please enter a valid option.")
                continue
            print("Data analyzed successfully.")
            return sorted_column
        except ValueError:
            print("Invalid input! Please enter a valid numeric value.")
