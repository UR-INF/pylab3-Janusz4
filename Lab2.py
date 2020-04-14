# fragmenty dotyczące rozwiązania poszczególnych zadań proszę oddzielić odpowiednimi komentarzami

# Zadanie 2. Napisz skrypt wypełniający tablicę znakami, a następnie wyświet znaki w kolejności odwrotnej do wprowadzania. Dane wprowadzane z klawiatury.
from array import *

tab = array('u', [])            #deklaracja tablicy

znaki = input("Podaj znaki: ")  #pobranie znaków

i = 0
while i < len(znaki):           #dodanie znakow do tablicy
    tab.append(znaki[i])
    i += 1

print("Podane znaki w odwrotnej kolejnosci: ", end="")
tab.reverse()                   #odwrócenei tablicy
i =0
while i < len(tab):             #wypisanie znaków
    print(tab[i], end="")
    i += 1
print()

# Zadanie 3. Wypełniający tablicę liczbami losowymi rzeczywistymi z przedziału (-5,5). Wartość tablicy zapisz do pliku result.txt
import random

tab = array('i', [])                    #deklaracja tablicy
for i in range(5):
    tab.append(random.randint(-5,5))    #wypełnianie tablicy losowymi liczbami
plik = open("result.txt","w")
i = 0
while i < len(tab):
    plik.write(str(tab[i]) + " ")       #zapis do pliku
    i += 1

plik.close()

# Zadanie 4, Napisz funkcję tworzącą tablicę dwuwymiarową (5x5) która zostanie wypełniona kwadratami liczb z komórek z wiersza wcześniejszego. Pierwszy wiersz wypełniony wartościami 2,3,4,5,6. Do utworzenia tablicy dwuwymiarowej wykorzystaj bibiotekę NumPy.
import numpy as np

def fun():
    tab = np.array(
        [[2, 3, 4, 5, 6], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])  # tworzenie tablicy 5x5
    i = 1
    while i < 5:
        for j in range(5):
            tab[i][j] = pow(tab[i - 1][j], 2)                                                   # wypełnianie tablicy
        i += 1
    return tab

print(fun())

# Zadanie 5. Napisz funkcję, która jako parametr przyjmuje lokalizację pliku tekstowego który zawiera dowolny tekst i zwraca histogram znaków występujących w tym napisie (czyli pary znak-liczba wystąpień). Wynikiem powinien być słownik.
import collections

def histogram(nazwa):
    plik = open(nazwa,"r")
    text = plik.readline()
    c = collections.Counter(text)
    return c
print(histogram("document.txt"))