'''
# japon bayrağı;
from turtle import *
pensize(10)
shape("blank")
for x in range(2):
    fd(150)
    rt(90)
    fd(100)
    rt(90)
pencolor("red")
penup()     # çizim yapmadan şekil oluşsun diye
goto(75,-80)    # olşturulan şeklin tam ortasındaki koordinatlar
pendown()
fillcolor("red")
begin_fill()
circle(30)
end_fill()
'''
# trafik lambası;
from turtle import *
pensize(10)
shape("blank")

fillcolor("gray")
begin_fill()
for x in range(2):
    fd(100)
    rt(90)
    fd(250)
    rt(90)
end_fill()

pencolor("red")
penup()
goto(50,-80)
pendown()
fillcolor("red")
begin_fill()
circle(30)
end_fill()

pencolor("yellow")
penup()
goto(50,-155)
pendown()
fillcolor("yellow")
begin_fill()
circle(30)
end_fill()

pencolor("green")
penup()
goto(50,-230)
pendown()
fillcolor("green")
begin_fill()
circle(30)
end_fill()
