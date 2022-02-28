"""Mountain View."""


__author__ = "730480631" 

from turtle import Turtle, colormode, done
colormode(255)


def main() -> None:
    """The entrypoint of my scene."""
    # Declare your Turtle variable(s) here.
    mountain: Turtle = Turtle() 
    grasss: Turtle = Turtle() 
    sun: Turtle = Turtle()  
    sky: Turtle = Turtle() 
    # Call the procedures you define and pass your Turtle(s) as an argument.
    background(sky, -400, 400, 800, 400)
    circle(sun, -200, 100)
    draw_mountain(mountain, -100, -100)
    draw_mountain(mountain, -300, -100)
    grass(grasss, -400, -100, 800, 400)

    done()

# Define the procedures for other components in your scene here.


def background(sky: Turtle, x: float, y: float, lenght: float, width: float) -> None: 
    """The blue sky background."""
    sky.penup()
    sky.goto(x, y)  
    sky.pendown() 
    sky.color(87, 218, 233)
    sky.begin_fill()
    i: int = 0 
    while i < 2: 
        sky.forward(800) 
        sky.right(90) 
        sky.forward(800) 
        sky.right(90) 
        i += 1 
   
    sky.hideturtle()
    sky.end_fill()


def draw_mountain(mountain: Turtle, x: float, y: float) -> None: 
    """A triangle mountain."""
    mountain.penup()
    mountain.pencolor(154, 177, 179)
    mountain.goto(x, y) 
    mountain.pendown() 
    mountain.color(154, 177, 179)
    mountain.begin_fill()
    i: int = 0 
    while (i < 3): 
        mountain.forward(300)
        mountain.left(120)
        i += 1

    mountain.hideturtle()
    mountain.end_fill()  


def grass(grasss: Turtle, x: float, y: float, lenght: float, width: float) -> None: 
    """The rectangle at the bottom(grass)."""
    grasss.penup()
    grasss.goto(x, y)  
    grasss.color(48, 203, 85) 
    grasss.begin_fill()
    grasss.pendown() 
    rectangle(grasss, x, y, lenght, width) 
   
    grasss.hideturtle()
    grasss.end_fill()  


def rectangle(rectangle: Turtle, x: float, y: float, lenght: float, width: float) -> None: 
    """Draws the rectangle when needed."""
    i: int = 0 
    while i < 2: 
        rectangle.forward(lenght) 
        rectangle.right(90) 
        rectangle.forward(width) 
        rectangle.right(90) 
        i += 1 


def circle(sun: Turtle, x: float, y: float) -> None: 
    """Drawing the sun (circle)."""    
    sun.penup() 
    sun.goto(x, y)
    sun.pendown()
    sun.color(245, 146, 49)
    sun.begin_fill()
    
    r: int = 100
    sun.circle(r)
    sun.hideturtle() 
    sun.end_fill() 


if __name__ == "__main__":
    main()