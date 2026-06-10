import math 

print('Program oblicza całki fukcnji sin(x)')
poczatek_zakresu = float(input('Podaj początek zakresu ')) #a
koniec_zakresu = float(input('Podaj koniec zakresu ')) #b

liczba_punktów = int(input('Podaj liczbę punktów')) #n + 1

krok = (koniec_zakresu - poczatek_zakresu)/(liczba_punktów - 1) #h

wybor = int(input('Jaką metodą chcesz całkować?\n1 -> Metoda Prostokątów\n2 -> Metoda Trapezów\n3 -> Metoda Simpsona(Metoda Parabol)\n4 -> Wszytskie trzy\n'))

tablica_punktów = []

tablica_sin = []

tablica_pol_p = []

tablica_pol_t = []

tablica_pol_s = []

#funckcja -> sin(x)

#tworzenie tablicy punktów
for i in range (liczba_punktów):
    punkt = poczatek_zakresu + i * krok
    #print(punkt)
    tablica_punktów.append(punkt) 


#tworzenie tablicy sinusów
for i in range (len(tablica_punktów)):
   sin =  math.sin(tablica_punktów[i])
   tablica_sin.append(sin)

#print(tablica_sin)

#wybór
if wybor == 1:
    #całkowanie Metoda Prostokątów
    for i in range (len(tablica_sin)-1):
        pole = krok * tablica_sin[i]
        tablica_pol_p.append(pole)
    
    calka = sum(tablica_pol_p)
    print('Całka z sin(x), z przedziału [',poczatek_zakresu , ',' ,koniec_zakresu,'] obliczona Metodą Prostokątów wynosi: ', calka)

    
elif wybor == 2:
    #całkowanie Metoda Trapezów
    for i in range (len(tablica_sin)-1):
        pole = ((tablica_sin[i] + tablica_sin[i+1])/2)*krok
        tablica_pol_t.append(pole)
    
    calka = sum(tablica_pol_t)
    print('Całka z sin(x), z przedziału [',poczatek_zakresu , ',' ,koniec_zakresu,'] obliczona Metodą Trapezów wynosi: ', calka)  

elif wybor == 3:
    #całkowanie Metoda Simpsona
    if (liczba_punktów - 1) % 2 == 0:   # n musiby być parystą, wiec jeeli liczba punktów (n+1) nie jest parysta to n jest paryste
        for i in range (0, len(tablica_sin)-2, 2):
            pole = ((tablica_sin[i]+4*tablica_sin[i+1]+tablica_sin[i+2])/3)*krok
            tablica_pol_s.append(pole)
        
        calka = sum(tablica_pol_s)  
        print('Całka z sin(x), z przedziału [',poczatek_zakresu , ',' ,koniec_zakresu,'] obliczona Metodą Simsona (Metodą Paraboli) wynosi: ', calka)

    else:
        print('Nie możemy wykonać Metody Simpsona bo liczba przediałów jest nieparysta, spróbój ponownie z liczba parzystą, lub z innymi metodami')
    

elif wybor == 4:

    #całkowanie Metoda Prostokątów
    for i in range (len(tablica_sin)):
        pole = krok * tablica_sin[i]
        tablica_pol_p.append(pole)
    calka = sum(tablica_pol_p)
    print('Całka z sin(x), z przedziału [',poczatek_zakresu , ',' ,koniec_zakresu,'] obliczona metodą prostokątów wynosi: ', calka)
    
    #całkowanie Metoda Trapezów
    for i in range (len(tablica_sin)-1):
        pole = ((tablica_sin[i] + tablica_sin[i+1])/2)*krok
        tablica_pol_t.append(pole)
    calka = sum(tablica_pol_t)
    print('Całka z sin(x), z przedziału [',poczatek_zakresu , ',' ,koniec_zakresu,'] obliczona Metodą Trapezów wynosi: ', calka)

    #całkowanie Metoda Simpsona
    if (liczba_punktów - 1) % 2 == 0:   # n musiby być parystą, wiec jeeli liczba punktów (n+1) nie jest parysta to n jest paryste
        for i in range (0, len(tablica_sin)-2, 2):
            pole = ((tablica_sin[i]+4*tablica_sin[i+1]+tablica_sin[i+2])/3)*krok
            tablica_pol_s.append(pole)
        calka = sum(tablica_pol_s)  
        print('Całka z sin(x), z przedziału [',poczatek_zakresu , ',' ,koniec_zakresu,'] obliczona Metodą Simsona (Metodą Paraboli) wynosi: ', calka)
    else:
        print('Nie możemy wykonać Metody Simpsona bo liczba przediałów jest nieparysta, spróbój ponownie z liczba parzystą, lub z innymi metodami')
    

    

    

