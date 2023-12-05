def alan(u,k):
    a=u*k
    return a
def cevre(u,k):
    c=(u+k)*2
    return c
u=int(input("uzun kenar:"))
k=int(input("kısa kenar:"))
print("alan",alan(u,k))
print("çevre",cevre(u,k))
