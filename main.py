def main():
    hexa_color = input("Enter the color for the hexagon: ")
    square_color = input("Enter the color for the square: ")
    circle_color = input("Enter the color for the circle: ")
    border_color = input("Enter the color for the border: ")

    window = Screen()
    turta = Turtle()

    setPos(turta, -250, 100)
    pattern(turta, hexa_color, circle_color, square_color, border_color)
    setPos(turta, -150, 0)
    pattern(turta, hexa_color, circle_color, square_color, border_color)
    setPos(turta, -50, -100)
    pattern(turta, hexa_color, circle_color, square_color, border_color)

    window.exitonclick
    
    


main()