from turtle import Turtle, colormode, done 
leo: Turtle = Turtle() 

leo.speed(50) 

leo.penup()
leo.goto(-150, -100) 
leo.pendown() 
colormode(255)
leo.color(99, 204, 250)


# code for shape to be filled


# leo.pencolor("pink")
# leo.fillcolor(32, 67, 93)
leo.color("purple")
leo.begin_fill() 


i: int = 0 
while (i < 3): 
    leo.forward(300)
    leo.left(120)
    i += 1

leo.hideturtle()
leo.end_fill()  
done()


bob: Turtle = Turtle() 
bob.penup()
bob.goto(-150, -100) 
bob.pendown()
