def toplama():
    global a
    global b
    a=5
    b=6
    return(a+b)
def cikarma():
    return(a-b)
def carpma():
    pass        # boş döndürme örneği
def bölme():
    return      # boş döndürme örneği
print("toplam:",toplama())
print("fark:",cikarma())
print("çarpım:",carpma())
print("bölüm:",bölme())
