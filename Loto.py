__author__ = 'u269074'

from random import randint

odgovor = int(raw_input("Koliko stevil zelis? "))

def loterija(kolicina):
    loto = []
    for nakljucno_stevilo in range (0, kolicina):
        nakljucno_stevilo = randint(0,9)
        loto.append(nakljucno_stevilo)
    print(loto)

loterija(odgovor)