#!/usr/bin/env python3
class kwiat():
    def __init__(self, kolor, nazwa):
        self.kolor = kolor
        self.nazwa = nazwa

def okr():
        print("Cześć, kolor kwiata to {} a jego nazwa to {}.".format(
            kwiat.kolor, kwiat.nazwa
        ))


kolor = input("Jaki jest kolor kwiata? ")
nazwa = input("Jak sie kwiat nazywa? ")
kwiat = kwiat(kolor, nazwa)
okr()
