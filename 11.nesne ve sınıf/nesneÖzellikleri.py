class araba():
    def __init__(self,model,marka,renk):      # metotlar, initte 2'şer tane alt çizgi var.
        self.model=model
        self.marka=marka        # bunlar başlangıç değerleridir.
        self.renk=renk

taksi=araba(1997,"opel","kırmızı")  
print(taksi.model)      # taksinin modelini yazdırdık
print(taksi.marka)
print(taksi.renk)
taksi.model=97          # modeli değiştirdik
print(taksi.model)

kamyon=araba(2012,"man","beyaz")
