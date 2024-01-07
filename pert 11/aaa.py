
import turtle

t = turtle.Turtle()
t.pencolor("blue")
t.fillcolor("blue")
t.begin_fill()
t.circle(50)

for i in range(8):
  t.circle(100, 90)
  t.left(45)

t.end_fill()
t.hideturtle()

turtle.mainloop()
