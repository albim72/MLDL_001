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

cube = list(map(lambda x:x**3,liczba))
print(cube)

kwadraty = [i**2 for i in range(5,5000,5)]
print(kwadraty)

#użycie modułów
import funkcje.bfunkcje as bf


def witaj(imie):
    return f'Miło Cię widzieć {imie}'

def osoba(funkcja,*args):
    return funkcja(*args)

print(osoba(witaj,"Olaf"))

print(osoba(bf.konkurs,"Anna",66,13))

print(osoba(bf.bonus,78,10))
