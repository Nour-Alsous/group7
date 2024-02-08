def circle(turta, circle_color, border_color):
    turta.color(border_color, circle_color)
    turta.begin_fill()

    turta.circle(45)

    turta.end_fill()


def pattern(turta, hexa_color, circle_color, square_color, border_color):

    hexagon(turta, hexa_color, border_color)

    move(turta, 150)

    circle(turta, circle_color, border_color)
    
    move(turta, 80)

    square(turta, square_color, border_color)

    