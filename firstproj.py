import turtle

wn = turtle.Screen()


fred = turtle.Pen()
fred.shape("turtle")
fred.fd(100)
fred.circle(100)
fred.color("blue")
fred.circle(-100)
fred.fd(100)

wn.exitonclick()