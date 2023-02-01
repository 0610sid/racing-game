import turtle

def makeTracks(abc):
    pen = turtle.RawTurtle(abc)
    pen.speed(0)

    pen.penup()
    pen.goto(-640,150)
    pen.pendown()

    for i in range(1,26) :
        if i==25 :
            pen.write("FINSIH")
        else:
            pen.write(i)
        pen.setheading(-90)
        pen.forward(300)
        pen.back(300)
        pen.penup()
        pen.setheading(0)
        pen.forward(50)
        pen.down()