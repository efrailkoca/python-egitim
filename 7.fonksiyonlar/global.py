# alt program;
def topla():
    global a # değişkeni tanımladığımız yerde atama yapamayız.
    a=5
    b=6
    return(a+b)

# ana program;
print(topla())
print(a) # fonksiyonun içerisinde global yaptığımız için çalışır.
print(b) # yerel olduğu için kod çalışmaz.
