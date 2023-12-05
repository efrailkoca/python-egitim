class araba():
    def __init__(self,model,marka,renk):
        self.model=model
        self.marka=marka        
        self.renk=renk
    def aracBilgisi(self):      # hiç parametre yazmasak bile self'i yazmamız gerekiyor.
        print("markası:",self.marka)
        print("modeli:",self.model)
        print("rengi:",self.renk)

taksi=araba(1997,"opel","kırmızı")
print("\ntaksi bilgisi")
taksi.aracBilgisi()
kamyon=araba(2010,"man","siyah")
print("\nkamyon bilgisi")
kamyon.aracBilgisi()

print("\n",dir(taksi))
