from math import *      # math modülündeki bütün fonk'ları çağırdık.

class kup:
    def __init__(self,a):
        self.a=a
    def yAlan(self):
        return(6*pow(self.a,2))
    def hacim(self):
        return(pow(self.a,3))

class kure:
    def __init__(self,r):
        self.r=r
    def yAlan(self):
        return("yüzey alanı:",4*pi*pow(self.r,2))
    def hacim(self):
        return((4/3)*pi*pow(self.r,3))

class silindir:
    def __init__(self,r,h):
        self.r=r
        self.h=h
    def yAlan(self):
        return(2*pi*self.r(self.r+self.h))  # (2*pi*pow(r,2))+(2*pi*r*h)
    def hacim(self):
        return(pi*pow(self.r,2)*self.h)

futbolTopu=kure(10)         # futbol topu nesnesi - class kure
pinponTopu=kure(3)          # pinpon topu nesnesi - class kure

kupSeker=kup(2)             # küp şeker nesnesi - class kup
koli=kup(50)                # koli nesnesi - class kup

merdane=silindir(3,30)      # merdane nesnesi - class silindir
tenccere=silindir(15,20)    # tencere nesnesi - class silindir
lastik=silindir(30,20)      # lastik nesnesi - class silindir
