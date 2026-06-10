import random
import math

wybor = int(input('1 -> Generator liczb pseudolosowych\n2 -> Obliczanie liczby Pi metodą Monte Carlo\n3 -> Obliczanie  wyznaczanie całki oznaczonej wskazanej funkcji we wskazanych granicach metodą Monte Carlo\n'))

if wybor == 1:

    n = int(input('Podaj ilość prób: '))
    p = int(input('Podaj początek zakresu: '))
    k = int(input('Podaj koniec zakresu: '))

    #Generowanie liczb w przedziale podanym przez użytkownika, ale randint podaje tylko liczby całkowite
    for _ in range(n):
        x = random.randint(p,k)

        print(x)

elif wybor == 2:
    n = int(input('Podaj ilość prób: '))

    trafienia = 0

    ##Generowanie liczb w przedziale [0,1]
    for _ in range(n):
        x = random.random()
        y = random.random()

        if x**2 + y**2 <= 1:
            trafienia += 1

    procent = (trafienia * 100) / n
    pi = 4 * trafienia / n

    print('\nIlośc punktów które mieszczą się w ćwiartce: ', trafienia ,'\nilość prób: ', n ,'\nProcent naszego koła: ', procent, '%\nPrzybliżenie π: ', pi) 


elif wybor == 3:

    n = int(input('Podaj ilość prób: '))
    p = float(input('Podaj początek zakresu: '))
    k = float(input('Podaj koniec zakresu: '))

    trafienia = 0

    #Maksymalna wartość sin(x) na przedziale [0, π]
    max_sin = 1

    #Generowanie liczb losowych w przedziale podanym przez użytkownika, ale uniform podaje tylko liczby rzeczywiste
    for _ in range(n):

        x = random.uniform(p,k)
        y = random.uniform(0, max_sin)

        if y <= math.sin(x):
            trafienia += 1

    pole_prostokata = (k - p) * max_sin

    calka = pole_prostokata * trafienia / n

    print('\nLiczba trafień: ', trafienia,'\nPrzybliżona wartość całki: ', calka)