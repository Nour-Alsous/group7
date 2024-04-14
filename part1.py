import csv

#Intro remarks
def intro():
    print("----------------------------")
    print("Welcome to Data Analysis CLI")
    print("----------------------------")
    print("Program stages:\n1. Load Data \n2. Clean and prepare data\n3. Analyse Data\n4. Visualize Data")
    print("Stage 1: Load Data")

#Loading data function- looped process incase of invalidity
def stage1():
    while True:
        file_path = input("Enter the path to the CSV file: ")
        try:
            with open(file_path, 'r') as file:
                reader = csv.reader(file)
                data = list(reader)
                for row in data:
                    print(row)
                columns = data[0]
                print("Columns in the CSV file:")
                for i in range(len(columns)):
                    print(str(i+1)+ '.' + columns[i])

                choice = int(input("Choose the column to process: ")) - 1
                if not choice in range(len(columns)):
                    print("Invalid choice! Please choose a valid column.")
                    continue
                selected_column = [row[choice] for row in data[1:]]
                print("Data loaded successfully.")
                return selected_column
        except FileNotFoundError:
            print("File not found! Please enter a valid file path.")
        except ValueError:
            print("Invalid input! Please enter a valid column number.")