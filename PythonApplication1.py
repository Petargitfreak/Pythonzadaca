import random
from collections import Counter

lista = [random.randint(0, 30) for _ in range(100)]
print("Generirana lista:")
print(lista)


brojac = Counter(lista)

print("\nElementi koji se pojavljuju 3 ili vi�e puta:")
for broj, count in brojac.items():
    if count >= 3:
        print(f"{broj} -> {count} puta")

######################################################################
def filtriraj_po_visini(rjecnik, granicna_visina):
    novi_rjecnik = {}
    
    for ime, visina in rjecnik.items():
        if visina > granicna_visina:
            novi_rjecnik[ime] = visina
    
    return novi_rjecnik



osobe = {
    'Pero Peric': 175,
    'Marko Markic': 180,
    'Jure Juric': 165,
    'Marija Maric': 190
}


rezultat = filtriraj_po_visini(osobe, 170)
print(rezultat)
#######################################################################
import random

def loto642():
    brojevi = random.sample(range(1, 43), 7)   
    return brojevi[:6], brojevi[6]             




igrac = []
print("Unesite 6 brojeva od 1 do 42:")
for _ in range(6):
    n = int(input("Broj: "))
    igrac.append(n)


glavni, dopunski = loto642()

print("\nIzvučeni brojevi:", glavni)
print("Dopunski broj:", dopunski)
print("Vaši brojevi:", igrac)


pogodci = [b for b in igrac if b in glavni or b == dopunski]
broj_pogodaka = len(pogodci)

print("\nUkupan broj pogodaka:", broj_pogodaka)

if pogodci:
    print("Pogođeni brojevi:", pogodci)
    print("Suma pogođenih:", sum(pogodci))
    print("Min pogođeni:", min(pogodci))
    print("Max pogođeni:", max(pogodci))
else:
    print("Nema pogođenih brojeva.")

###################################################################
import random


lista = [random.randint(1, 999) for _ in range(50)]
print("Lista:", lista)


frekvencije = {}


for broj in lista:
    for znamenka in str(broj):     
        z = int(znamenka)          
        if z not in frekvencije:
            frekvencije[z] = 0
        frekvencije[z] += 1

print("Frekvencije znamenki:", frekvencije)
#############################################################################
x, y = 5, 7


putanja = input("Unesite putanju robota (npr. SJIJI): ")

for naredba in putanja:
    if naredba == "S":       
        y += 3
    elif naredba == "J":     
        y -= 1
    elif naredba == "I":     
        x += 1
    elif naredba == "Z":     
        x -= 1
    else:
        print(f"Ignoriram nepoznatu naredbu: {naredba}")


print(f"Konačna pozicija robota je: ({x}, {y})")

#############################################################################
import math


r = float(input("Unesite radijus kružnice r: "))
a = float(input("Unesite koordinatu a (x središta): "))
b = float(input("Unesite koordinatu b (y središta): "))

broj_tocaka = 0
pogodaka = 0

print("\nUnesite po jednu točku (x y). Za kraj unesite 0 0.\n")

while True:
    x, y = map(float, input("Točka: ").split())

    
    if x == 0 and y == 0:
        break

    broj_tocaka += 1

    
    lijeva_strana = (x - a)**2 + (y - b)**2

    
    if math.isclose(lijeva_strana, r**2, rel_tol=1e-6, abs_tol=1e-6):
        pogodaka += 1
        print(" → Točka JE na kružnici.")
    else:
        print(" → Točka NIJE na kružnici.")


if broj_tocaka > 0:
    omjer = (pogodaka / broj_tocaka) * 100
    print(f"\nUkupan broj točaka: {broj_tocaka}")
    print(f"Broj pogodaka kružnice: {pogodaka}")
    print(f"Omjer pogodaka: {omjer:.2f}%")
else:
    print("Nije unesena nijedna točka prije (0,0).")
################################################################
studenti = {
    'ivan': (3, 2, 4),
    'marko': (5, 5, 4),
    'ana': (2, 3, 4)
}

def grupiraj_po_prosjeku(d):
    rezultat = {}

    for ime, ocjene in d.items():
        prosjek = round(sum(ocjene) / len(ocjene))  
        
        if prosjek not in rezultat:
            rezultat[prosjek] = []
        
        rezultat[prosjek].append(ime)

    
    for ključ in rezultat:
        rezultat[ključ].sort()

    return rezultat


izlaz = grupiraj_po_prosjeku(studenti)
print(izlaz)
######################################################################
def grupiraj_stringove(lista):
    rezultat = {}

    for s in lista:                  
        for znak in s:               
            if znak not in rezultat:
                rezultat[znak] = []
            rezultat[znak].append(s)

    return rezultat



ulaz = ['dobar', 'dan']
izlaz = grupiraj_stringove(ulaz)
print(izlaz)
#########################################################################
def nenumericki_elementi(matrica):
    rezultat = {}

    for x in range(len(matrica)):            
        for y in range(len(matrica[x])):     
            element = matrica[x][y]

            
            if not element.isdigit():
                rezultat[(x, y)] = element

    return rezultat



matrica = [
    ["5", "4", "a", "1"],
    ["c", "3", "12", "b"],
    ["7", "9", "0", "d"]
]

print(nenumericki_elementi(matrica))
########################################################################
def broj_stringova(lista):
    brojac = 0

    for s in lista:
        if len(s) >= 3:                 
            prva = s[0]                 
            if s.count(prva) >= 2:      
                brojac += 1

    return brojac



ulaz = ['abc', 'aba', 'cc', 'ijki']
print(broj_stringova(ulaz))   
