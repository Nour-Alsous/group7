def stage4(column):
    print("Visualizing data:")
    for value in column:
        stars = int(int(value) / 5)
        if stars > 20:
            stars = 20
        print(value + ": " + '*' * stars)
