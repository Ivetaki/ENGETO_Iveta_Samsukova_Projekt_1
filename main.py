"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Iveta Samšuková
email: i.samsukova@gmail.com
"""

TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

# Slovník registrovaných uživatelů
uzivatele = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

# Přihlášení
jmeno = input("Přihlašovací jméno: ")
heslo = input("Heslo: ")

print("-" * 40)

if jmeno not in uzivatele:
    print("Neregistrovaný uživatel. Přístup odepřen.")
elif uzivatele[jmeno] != heslo:
    print("Špatné heslo. Přístup odepřen.")
else:
    print("Ahoj " + jmeno + ", vítej v aplikaci pro analýzu textu.")
    print("K dispozici jsou tři texty k analýze.")
    print("-" * 40)

    vyber_textu = input("Zadej číslo textu (1–3): ")

    print("-" * 40)

    if vyber_textu.isdigit():
        cislo = int(vyber_textu)
        if 1 <= cislo <= 3:
            print("Vybral/a jsi text číslo: " + str(cislo))

            text = TEXTS[cislo - 1] # program vybere zvolený text

            slova = text.split()

            pocet_slov = len(slova)
            pocet_velkych_na_zacatku = 0 # počet slov začínajících velkým písmenem
            pocet_slov_velkymi = 0 # počet slov psaných velkými písmeny
            pocet_slov_malymi = 0 # počet slov psaných malými písmeny
            pocet_cisel = 0
            soucet_cisel = 0

            for slovo in slova:
                slovo = slovo.strip(",.?!")
                if slovo.istitle():
                    pocet_velkych_na_zacatku += 1
                if slovo.isupper():
                    pocet_slov_velkymi += 1
                if slovo.islower():
                    pocet_slov_malymi += 1
                if slovo.isdigit():
                    pocet_cisel += 1
                    soucet_cisel += int(slovo)
            
            print("-" * 40)
            print("Statistika:")
            print("Počet slov:", pocet_slov)
            print("Počet slov začínajících velkým písmenem:", pocet_velkych_na_zacatku)
            print("Počet slov psaných velkými písmeny:", pocet_slov_velkymi)
            print("Počet slov psaných malými písmeny:", pocet_slov_malymi)
            print("Počet čísel:", pocet_cisel)
            print("Suma všech čísel:", soucet_cisel)
            print("-" * 40)
            
            cetnosti = {} # četnost délek slov, {délka slova: počet slov této délky}
            for slovo in slova:
                slovo = slovo.strip(",.?!")
                delka = len(slovo)
                cetnosti[delka] = cetnosti.get(delka, 0) + 1

            print("DÉLKA|  VÝSKYT  |ČÍSLO")
            print("-" * 40)
            for delka in sorted(cetnosti):
                pocet = cetnosti[delka]
                print(str(delka) + "| " + "*" * pocet + " " + str(pocet))
        
        else:
            print("Text s tímto číslem neexistuje. Program končí.")
    else:
        print("To není platné číslo. Program končí.")