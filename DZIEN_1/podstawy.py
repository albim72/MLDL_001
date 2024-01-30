a=5
print(a)
print(type(a))

h:float = 145
print(h)
print(type(h))
print(id(h))

h = "jedynka"
print(h)
print(type(h))
print(id(h))

liczba = [4,6,3,6,2,78,43,78,36,11,93,16,-4,10,0,-3]

pozycje_parz = liczba[::2]
print(pozycje_parz)

la = liczba
print(id(la))
print(id(liczba))
print(id(pozycje_parz))

s = "lajkonik"
print(s)
print(s[0])
print(s[1])
print(s[-1])

print(s[::-1])

parzyste = list(filter(lambda x:x%2==0,liczba))

print(parzyste)
