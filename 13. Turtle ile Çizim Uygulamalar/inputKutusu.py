from turtle import*
n=int(numinput("poligon","kenar sayısı",5))
renk=textinput("renk","içrenk")

pensize(4)

begin_fill()
fillcolor(renk)
circle(100,360,n)
end_fill()
