import turtle
spiral=turtle.Turtle()
spiral.speed(500)
for i in range(100):
    spiral.backward(i)
    spiral.left(91)
    spiral.circle(i)
    spiral.fillcolor("red")
    spiral.forward(i)
    spiral.pencolor("blue")