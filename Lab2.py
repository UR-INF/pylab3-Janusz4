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
i =0 ;
while i < len(tab):             #wypisanie znaków
    print(tab[i], end="")
    i += 1
