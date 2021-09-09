import turtle

count=1

while (count<=6):
    turtle.pendown()
    turtle.forward(500)
    turtle.penup()
    turtle.goto(0,count*100)
    count+=1

turtle.home()
count=1
turtle.left(90)

while (count<=6):
    turtle.pendown()
    turtle.forward(500)
    turtle.penup()
    turtle.goto(count*100,0)
    count+=1

turtle.exitonclick   
