from turtle import *
pensize(50)
color("red","yellow")       # 1.renk : kenar rengi  2.renk : iç renk
def ucgen():
    for x in range(3):
        fd(200)
        lt(120)

begin_fill()        # rengi doldurmaya başla
ucgen()             # fonksiyonu çağır
end_fill()          # rengi doldurmayı sonlandır
