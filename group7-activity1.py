from turtle import Turtle, Screen
"""
NAME- MOHSIN - worked on main function, the move, and ran tests
      NOUR- worked on hexagon,the setpostion and pattern functions
      NABIL - worked on the square and circle
This module is programmed to code a pattern of hexagons,circles,and squares. The user is asked to input the colors they desire for
each shape and pen color. After that, the program prints out the shapes in the following pattern: hexagon,circle and finally square.It prints it
in a row then shifts down and print another row until 3 are drawn.
This is the link to our group7 repository on github https://github.com/Nour-Alsous/group7
"""

def setPos(turta, x, y): #this function makes the turta go to the point (x,y)  we want,                     
    turta.penup() #it specfies the starting point of the row. this allows us to make the three rows start at different positions and under each other
    turta.goto(x, y)
    turta.pendown()

def move(turta,m): #this function makes the turta raise its pen, move to the right, 
    turta.penup() #put its pen down and draw again this allows us to draw in a row 
    turta.forward(m)
    turta.pendown()

def hexagon(turta, hexa_color, border_color): #we defined a function that can draw a hexagon using the forward and left command mainly
    turta.color(border_color, hexa_color)
    turta.begin_fill()

    turta.forward(50)
    turta.left(60)

    turta.forward(50)
    turta.left(60)

    turta.forward(50)
    turta.left(60)

    turta.forward(50)
    turta.left(60)

    turta.forward(50)
    turta.left(60)
    
    turta.forward(50)
    turta.left(60)

    turta.end_fill()




def square(turta, square_color, border_color): #we defined a function that can draw the squares with mainly the forward an left commands
    turta.color(border_color, square_color)
    turta.begin_fill()

    turta.forward(90)
    turta.left(90)

    turta.forward(90)
    turta.left(90)

    turta.forward(90)
    turta.left(90)

    turta.forward(90)
    turta.left(90)

    turta.end_fill()


def circle(turta, circle_color, border_color):#this is the function for the circle that we coded
    turta.color(border_color, circle_color)
    turta.begin_fill()

    turta.circle(45)

    turta.end_fill()


def pattern(turta, hexa_color, circle_color, square_color, border_color): #here in the pattern we created an order in which the shapes will be drawn in.

    hexagon(turta, hexa_color, border_color)#first the hexagon will be drawn

    move(turta, 150)#then we move the function to the right

    circle(turta, circle_color, border_color) #we draw the circle
    
    move(turta, 80)#we move it forward

    square(turta, square_color, border_color)#we draw the square
#everytime the pattern function is called, it will draw the shapes in this order, creating a pattern

def main(): #in the main function,we asked for the user to input the colors they want for the shapes and pen
    
    
    hexa_color = input("Enter the color for the hexagon: ")  
    square_color = input("Enter the color for the square: ")
    circle_color = input("Enter the color for the circle: ")
    border_color = input("Enter the color for the border: ")

    window = Screen() #we assign window to screen to give it a name
    turta = Turtle() #we assigned turtle as turta
    window.bgcolor("pink")

#repitition this chunck allows us to set a specific postion and print the pattern then we repeat it while changin the value of each position to shift it down
    setPos(turta, -300, 120)
    pattern(turta, hexa_color, circle_color, square_color, border_color) #and then called every function inside the main function
    setPos(turta, -200, 0)
    pattern(turta, hexa_color, circle_color, square_color, border_color)
    setPos(turta, -100, -120)
    pattern(turta, hexa_color, circle_color, square_color, border_color)
    
    # we ask the code to not stop until the whole code is done, similar to turtle.done(), and only to exit once X is clicked
    window.exitonclick()
    
    


main()



