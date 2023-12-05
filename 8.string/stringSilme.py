yazi="python"
print(yazi[:-1])
print(yazi[:-2])
print(yazi[:-5])    # sondan kaçıncı indise kadar silineceğini belirlemek için.

for x in range(1,6):
    print(yazi[:-x])
print()

for x in range(6,0,-1):
    print(yazi[:-x])
print(yazi)
