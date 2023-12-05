# kısa yol;
'''
def ustel(t,u):
    return t**u
t=int(input("taban:"))
u=int(input("üst:"))
print(ustel(t,u))
'''

# özyinelemeli fonksiyon;
def ustel(t,u):
    if u==0:
        return 1
    else:
        return t*ustel(t,u-1) # 2*2*2*2*1
t=int(input("taban:"))
u=int(input("üst:"))
print(ustel(t,u))

