'''
from turtle import *
n=int(input("köşe sayısı:"))
aci=360/n
pensize(2)
for x in range(n):
    fd(100)
    lt(aci)
'''
from turtle import *
circle(50,360,5)    # 1:uzunluk     2:açı    3:köşegen sayısı
