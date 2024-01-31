class Book:
    #deklaracja stanu:
    # def __new__(cls, *args, **kwargs):
    #     return object.__new__(Book)

    def __init__(self,id,tytul,autor,cena=30):
        self.idbook = id
        self.tytul = tytul
        self.autor = autor
        self.cena = cena
        self.oprawa = "miękka"
        self.create_book()

    def __repr__(self):
        return (f'książka {self.tytul}, autor: {self.autor}, cena: {self.cena} zł, '
                f'oprawa: {self.oprawa}')

    def create_book(self):
        print("utworzenie nowego obiektu klasy Book")

    def rabat(self,procent):
        return self.cena*(procent/100)

bk=Book(89,"Wiedźmin","Andrzej Sapkowski")
print(bk)
print(f'Rabat: {bk.rabat(25)} zł')
bk.oprawa = "twarda"
print(f'oprawa po zmianie: {bk.oprawa}')
