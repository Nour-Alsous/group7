def stage2(column):
    while True:
        try:
            print(column)
            replacement_option = int(input("Choose replacement option for empty cells:\n"
                                           "1. Minimum value\n"
                                           "2. Maximum value\n"
                                           "3. Average value\n"
                                           "Enter your choice: "))
            if replacement_option == 1:
                replacement_value = int(column[0])
                for val in column:
                    if val and int(val) < replacement_value:
                         replacement_value = int(val)
            elif replacement_option == 2:
                    replacement_value = int(column[0])
                    for val in column:
                        if val and int(val) > replacement_value:
                            replacement_value = int(val)
            elif replacement_option == 3:
                    values = [int(val) for val in column if val]
                    replacement_value = sum(values) / len(values)

            else:
                print("Invalid choice! Please enter a valid option.")
                continue
            for i in range(len(column)):
                if column[i] == '':
                 column[i] = replacement_value
                else:
                 column[i] = int(column[i])

            print("Data cleaned and prepared successfully.")
            return column
        except ValueError:
            print("Invalid input! Please enter a valid numeric value.")