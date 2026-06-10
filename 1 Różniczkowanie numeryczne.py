import math
import matplotlib.pyplot as wykres

print('Program oblicza pochodną fukcnji sin(x)')
poczatek_zakresu = float(input('Podaj początek zakresu '))
koniec_zakresu = float(input('Podaj koniec zakresu '))

liczba_punktow = int(input('Podaj liczbę punktów '))

wybor = int(input('Jaką metodą chcesz różniczkować?\n1 -> Metoda Progresywna\n2 -> Metoda centralna\n3 -> Metoda wsteczna\n4 -> Wszytskie trzy\n'))

krok = (koniec_zakresu - poczatek_zakresu)/(liczba_punktow - 1)

tablica_punktow = []

tablica_sin = []

tablica_pochodnych_c = []

tablica_pochodnych_p = []

tablica_pochodnych_w = []


#funckcja -> sin(x)

#tworzenie tablicy punktów
for i in range (liczba_punktow):
    punkt = poczatek_zakresu + i * krok
    #print(punkt)
    tablica_punktow.append(punkt)

#print(tablica_punktow)   


#tworzenie tablicy sinusów
for i in range (len(tablica_punktow)):
   sin =  math.sin(tablica_punktow[i])
   tablica_sin.append(sin)

#print(tablica_sin)

#wybór
if wybor == 1:
    #różniczkowanie metoda progresywan
    for i in range (len(tablica_sin)-1):
        pochodna = (tablica_sin[i+1] - tablica_sin[i])/ krok
        tablica_pochodnych_p.append(pochodna)
    
    wykres.figure()
    wykres.plot(tablica_punktow[:-1], tablica_pochodnych_p, 'r-',label='Metoda Progresywan')
    wykres.plot(tablica_punktow, tablica_sin, 'b-', label='Funkcja sin(x)')
    wykres.xlabel('x')
    wykres.ylabel('pochodna')
    wykres.title('Metoda Progresywan')
    wykres.legend()
    wykres.grid(True)
    wykres.show()
    
elif wybor == 2:
    #różniczkowanie metoda centralna
    for i in range (1,len(tablica_sin)-1):
        pochodna = (tablica_sin[i+1] - tablica_sin[i-1])/(2 * krok)
        tablica_pochodnych_c.append(pochodna)

    wykres.figure()
    wykres.plot(tablica_punktow[1:-1], tablica_pochodnych_c, 'r-',label='Metoda Centralna')
    wykres.plot(tablica_punktow, tablica_sin, 'b-', label='Funkcja sin(x)')
    wykres.xlabel('x')
    wykres.ylabel('pochodna')
    wykres.title('Metoda Centralna')
    wykres.legend()
    wykres.grid(True)
    wykres.show()  

elif wybor == 3:
    #różniczkowanie metoda wsteczna
    for i in range (1,len(tablica_sin)):
        pochodna = (tablica_sin[i] - tablica_sin[i-1])/ krok
        tablica_pochodnych_w.append(pochodna)

    wykres.figure()
    wykres.plot(tablica_punktow[1:], tablica_pochodnych_w, 'r-',label='Metoda Wsteczna')
    wykres.plot(tablica_punktow, tablica_sin, 'b-', label='Funkcja sin(x)')
    wykres.xlabel('x')
    wykres.ylabel('pochodna')
    wykres.title('Metoda Wsteczna')
    wykres.legend()
    wykres.grid(True)
    wykres.show() 

elif wybor == 4:
    #różniczkowanie metoda progresywan
    for i in range (len(tablica_sin)-1):
        pochodna = (tablica_sin[i+1] - tablica_sin[i])/ krok
        tablica_pochodnych_p.append(pochodna)
    
    #różniczkowanie metoda centralna
    for i in range (1,len(tablica_sin)-1):
        pochodna = (tablica_sin[i+1] - tablica_sin[i-1])/(2 * krok)
        tablica_pochodnych_c.append(pochodna)

    #różniczkowanie metoda wsteczna
    for i in range (1,len(tablica_sin)):
        pochodna = (tablica_sin[i] - tablica_sin[i-1])/ krok
        tablica_pochodnych_w.append(pochodna)

    wykres.figure()
    wykres.plot(tablica_punktow[:-1], tablica_pochodnych_p, 'r-',label='Metoda Progresywana')
    wykres.plot(tablica_punktow[1:-1], tablica_pochodnych_c, 'g-',label='Metoda Centralna')
    wykres.plot(tablica_punktow[1:], tablica_pochodnych_w, 'y-',label='Metoda Wsteczna')
    wykres.plot(tablica_punktow, tablica_sin, 'b-', label='Funkcja sin(x)')
    wykres.xlabel('x')
    wykres.ylabel('pochodna')
    wykres.title('Wszystkie metody')
    wykres.legend()
    wykres.grid(True)
    wykres.show() 

    

    

    

