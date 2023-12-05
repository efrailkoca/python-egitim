# sadece karekök aldırmak için bütün math fonksiyonunu çağırmak mantıksız.
'''
import math
print(math.sqrt(9))     # sayının karekökünü aldırmak için.
'''
# diğer yol;
from math import sqrt
print(sqrt(9))

# başka yol;
from math import *      # tüm fonksiyonları çağırır. 1. yoldan farkı;'math.' yazmamıza gerek duydurtmaz.
print(sqrt(100))

# ismi farklı kullanmak için;
import math as m
print(m.sqrt(100))
