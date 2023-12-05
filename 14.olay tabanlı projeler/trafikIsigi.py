from turtle import*
import time     # bu modül zamanla ilgili çeşitli işlevler sağlar.
w=Screen()
w.setup(300,700)
w.title("trafik ışık uygulaması")

penup()
goto(0,180)
pendown()
pensize(4)

for i in range(2):
    fd(80)
    right(90)
    fd(220)
    right(90)

def kirmizi():
    penup()
    goto(40,140)
    fillcolor("red")
    shape("circle")
    shapesize(3)
def sari():
    penup()
    goto(40,70)
    fillcolor("yellow")
    shape("circle")
    shapesize(3)
def yesil():
    penup()
    goto(40,0)
    fillcolor("green")
    shape("circle")
    shapesize(3)

sayac=0
while True:
    kirmizi()
    time.sleep(2)
    sari()
    time.sleep(1)
    yesil()
    time.sleep(2)
    sayac+=1
    if sayac==3:
        break

w.mainloop()
