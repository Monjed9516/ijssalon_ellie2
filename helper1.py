def fooi_pp(bedrag, personen):
        bedrag_pp = bedrag / personen
        return bedrag_pp
        uitvoer = (f"Het {bedrag} per person is 10 euro")

b = int(input("Welk bedrag zit er in de fooienpot?"))
p = int(input("Over hoeveel mensen moet de pot verdeeld worden?"))

print(fooi_pp(b,p))