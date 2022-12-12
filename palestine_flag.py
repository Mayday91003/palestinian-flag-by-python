# Palestinian flag
from turtle import*
setup(800,400)
penup()
goto(-400,200)
pendown()

#black rectengle
color("black")
begin_fill()
forward(800)
right(90)
forward(133)
right(90)
forward(800)
right(180)
end_fill()

#white rectengle
color("white")
begin_fill()
forward(800)
right(90)
forward(133)
right(90)
forward(800)
right(180)
end_fill()

#green rectengle
color("green")
begin_fill()
forward(800)
right(90)
forward(133)
right(90)
forward(800)
right(180)
end_fill()

#red triangle
color("red")
begin_fill()
goto(-200,15)
left(318)
forward(-400)
end_fill()