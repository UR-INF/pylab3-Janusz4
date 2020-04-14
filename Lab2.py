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

