from turtle import*
pensize(3)
win=Screen()
win.setup(200)
penup()         # istediğimiz yerden başlamak için
def nokta(x,y):
    goto(x,y)
    pendown()   # istediğimiz yerden başlamak için

win.onclick(nokta)  # tıklama olduğunda nokta fonksiyonunu çalıştırır.
mainloop()
