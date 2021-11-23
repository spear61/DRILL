import turtle

def run_turtle(degree,distance=50):
    turtle.setheading(degree)
    turtle.forward(distance)
    turtle.stamp()

def move_w():
    run_turtle(90)

def move_a():
    run_turtle(180)

def move_s():
    run_turtle(270)

def move_d():
    run_turtle(0)    

def restart():
    turtle.reset()

turtle.shape("turtle")

turtle.onkey(move_w,'w')
turtle.onkey(move_a,'a')
turtle.onkey(move_s,'s')
turtle.onkey(move_d,'d')
turtle.onkey(restart,'Escape')
turtle.listen()

