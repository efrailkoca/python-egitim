import turtle,time,random

liste=[]
skor=0
maxSkor=0

#çerçeve ayarları
w=turtle.Screen()
w.title("yılan oyunu")
w.setup(600,600)
w.bgcolor("blue")
w.tracer(0)

# yılan kafa
yn=turtle.Turtle()
yn.speed(0)
yn.shape("circle")
yn.color("red")
yn.penup()
yn.goto(0,0)
yn.yon="dur"

#ilk ara

def hareket():
    if yn.yon=="ust":
        y=yn.ycor()     # y ekseninde yukarı git
        yn.sety(y+20)
    if yn.yon=="alt":
        y=yn.ycor()     # y ekseninde aşağı git
        yn.sety(y-20)
    if yn.yon=="sag":    
        x=yn.xcor()     # x ekseninde sağa ilerle
        yn.setx(x+20)
    if yn.yon=="sol":
        x=yn.xcor()     # x ekseninde sola ilerle
        yn.setx(x-20)

def yukariGit():
    if yn.yon!="alt":
        yn.yon="ust"
def asagiGit():
    if yn.yon!="ust":
        yn.yon="alt"
def sagaGit():
    if yn.yon!="sol":
        yn.yon="sag"
def solaGit():
    if yn.yon!="sag":
        yn.yon="sol"

w.listen()
w.onkeypress(yukariGit,"Up")
w.onkeypress(asagiGit,"Down")
w.onkeypress(sagaGit,"Right")
w.onkeypress(solaGit,"Left")

while True:
    w.update()
    hareket()
    time.sleep(0.1)

#ikinci ara

yem=turtle.Turtle()
yem.speed(0)
yem.shape("circle")
yem.color("red")
yem.penup()
yem.goto(0,100)


def ye():
    if yn.distance(yem)<20:
        x=random.randint(-280,280)
        y=random.randint(-280,280)
        yem.goto(x,y)

        kuyruk=turtle.Turtle()
        kuyruk.speed(0)
        kuyruk.shape("circle")
        kuyruk.color("pink")
        kuyruk.penup()
        liste.append(kuyruk)

        skor+=5
        if skor>maxSkor:
            maxSkor=skor
            w.title("skor:{} en yüksek skor:{}".format(skor,maxSkor))

#üçüncü ara
            
    uzunluk=len(liste)
    for indis in range(uzunluk-1,0,-1):
        x=liste[indis-1].xcor()
        y=liste[indis-1].ycor()
        liste[indis].goto(x,y)
    if len(liste)>0:
        x=yn.xcor()
        y=yn.ycor()
        liste=[0].goto(x,y)
def baslangic():
    time.sleep(0.1)
    yn.goto(0,0)
    yn.yon="dur"
    global skor
    for eklem in liste:
        eklem.goto(1000,1000)
    liste.clear()
    skor=0
    w.title("skor: {} en yüksek puan: {}".format(skor,maxSkor))

while True:
    w.update()
    ye()
    hareket()
    if yn.xcor()>290 or yn.xcor()<-290 or yn.ycor<-290:
        baslangic()
    for eklem in liste:
        if eklem.distence(yn)<20:
            baslangic()
    time.speed(0.1)

w.mainloop()






        
