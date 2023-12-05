from turtle import *

# kare cizim fonksiyonu
def kareCizim(mesafe):
    for a in range(1,5):
        forward(mesafe)
        left(90)

hideturtle()
pensize(2)
x=int(input("kare sayısı gir"))
for a in range(x):
    kareCizim(50*a)
    
kareCizim(50)
kareCizim(100)
kareCizim(150)
