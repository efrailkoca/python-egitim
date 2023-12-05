from turtle import *
colormode(255)
pensize(50)
color(255,100,255)      #1.sıfır:kırmızı    2.sıfır:yeşil   3.sıfır:mavi    tonlar ile rengi belirliyoruz.
def ucgen():
    for x in range(3):
        fd(200)
        lt(120)
def kare():
    for x in range(4):
        fd(200)
        rt(90)

begin_fill()
fillcolor(165,42,42)
ucgen()
end_fill()

begin_fill()
fillcolor(128,128,128)
kare()
end_fill()
