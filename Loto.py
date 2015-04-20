__author__ = 'u269074'

from random import randint

odgovor = int(raw_input("Koliko stevil zelis? "))

def loterija():
    loto = []
    for nakljucno_stevilo in range (0, odgovor):
        nakljucno_stevilo = randint(0,9)
        loto.append(nakljucno_stevilo)
    print(loto)

loterija()