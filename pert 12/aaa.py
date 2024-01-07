from turtle import *
turtle = Turtle()
screen = Screen()
list2 = ["red","purple","blue","green","orange","yellow"]
for i in range(int(input("how many times do you want to spin?"))):
  turtle.left(100)
  turtle.forward(i)
  turtle.color(list2[i % 6])
  turtle.width(i / 100 + 1)
  turtle.speed(100)