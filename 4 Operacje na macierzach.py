print('Kalkulator macierzy\nJakie działanie na macierzy chcesz zrobić?')
wybor = int(input('1 -> Dodawanie\n2 -> Odejmowanie\n3 -> Mnożenie przez skalar\n4 -> Mnożenie\n5 -> Transponowanie\n'))

print('Macierz A')
liczba_wierszy_A = int(input('Ile ma mieć wierszy macierz: ')) 
liczba_kolumn_A = int(input('Ile ma mieć kolumn macierz: '))

print('Macierz B')
liczba_wierszy_B = int(input('Ile ma mieć wierszy macierz: ')) 
liczba_kolumn_B = int(input('Ile ma mieć kolumn macierz: '))

# Funkcja tworząca macierz
def ksztalt(wiersze, kolumny):
    macierz = []
    for i in range(wiersze):
        macierz.append([])
        for j in range(kolumny):
            macierz[i].append(0)
    return macierz

# Tworzenie pustych macierzy
A = ksztalt(liczba_wierszy_A, liczba_kolumn_A)
B = ksztalt(liczba_wierszy_B, liczba_kolumn_B)

# Wypełnianie macierzy
def wypelnij(macierz, nazwa):
    for i in range(len(macierz)):
        for j in range(len(macierz[0])):
            macierz[i][j] = float(input(f'Podaj element {nazwa}[{i}][{j}]: '))
    return macierz

# Dodawanie
def dodawanie(A, B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        return print('Nie można dodać macierzy, różne wymiary')
    wiersze = len(A)
    kolumny = len(A[0])
    C = ksztalt(wiersze, kolumny)
    for i in range(wiersze):
        for j in range(kolumny):
            C[i][j] = A[i][j] + B[i][j]
    return C

# Odejmowanie
def odejmowanie(A, B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        return print('Nie można odjąć macierzy, różne wymiary')
    wiersze = len(A)
    kolumny = len(A[0])
    C = ksztalt(wiersze, kolumny)
    for i in range(wiersze):
        for j in range(kolumny):
            C[i][j] = A[i][j] - B[i][j]
    return C

# Mnożenie przez skalar
def mnozenie_przez_skalar():
    skalar = float(input('Podaj skalar: '))
    wybor_m = input('Którą macierz chcesz pomnożyć? A czy B: ')
    
    if wybor_m == 'A':
        macierz = A
    elif wybor_m == 'B':
        macierz = B
    else:
        print('Nie ma takiej macierzy')
    
    wiersze = len(macierz)
    kolumny = len(macierz[0])
    C = ksztalt(wiersze, kolumny)
    for i in range(wiersze):
        for j in range(kolumny):
            C[i][j] = skalar * macierz[i][j]
    return C, wybor_m, skalar

# Mnożenie macierzy
def mnozenie(A, B):
    if len(A[0]) != len(B):
        return print('Nie można pomnożyć macierzy, liczba kolumn A musi równać się liczbie wierszy B')
    wiersze = len(A)
    kolumny = len(B[0])
    C = ksztalt(wiersze, kolumny)
    for i in range(wiersze):
        for j in range(kolumny):
            suma = 0
            for k in range(len(A[0])):
                suma += A[i][k] * B[k][j]
            C[i][j] = suma
    return C

# Transponowanie
def transponowanie():
    wybor_t = input('Jaką macierz chcesz transponować? A czy B: ')
    if wybor_t == 'A':
        macierz = A
    elif wybor_t == 'B':
        macierz = B
    else:
        print('Nie ma takiej macierzy')
    
    wiersze = len(macierz)
    kolumny = len(macierz[0])
    C = ksztalt(kolumny, wiersze)
    for i in range(wiersze):
        for j in range(kolumny):
            C[j][i] = macierz[i][j]
    return C, wybor_t

# Wyświetlanie
def wyswietlanie(macierz, nazwa):
    print(f'\n{nazwa}:')
    for wiersz in macierz:
        print(wiersz)

# Wypełnianie macierzy
print('\nWypełnianie macierzy A:')
wypelnij(A, 'A')
print('\nWypełnianie macierzy B:')
wypelnij(B, 'B')

# Wykonanie wybranej operacji
if wybor == 1:
    wynik = dodawanie(A, B)
    if wynik:
        wyswietlanie(A, 'Macierz A')
        wyswietlanie(B, 'Macierz B')
        wyswietlanie(wynik, 'Wynik dodawania')
        
elif wybor == 2:
    wynik = odejmowanie(A, B)
    if wynik:
        wyswietlanie(A, 'Macierz A')
        wyswietlanie(B, 'Macierz B')
        wyswietlanie(wynik, 'Wynik odejmowania')
        
elif wybor == 3:
    wynik, wybrana, skalar = mnozenie_przez_skalar()
    if wynik:
        if wybrana == 'A':
            wyswietlanie(A, 'Macierz A')
        else:
            wyswietlanie(B, 'Macierz B')
        wyswietlanie(wynik, f'Wynik mnożenia macierzy {wybrana} przez {skalar}')
        
elif wybor == 4:
    wynik = mnozenie(A, B)
    if wynik:
        wyswietlanie(A, 'Macierz A')
        wyswietlanie(B, 'Macierz B')
        wyswietlanie(wynik, 'Wynik mnożenia')
        
elif wybor == 5:
    wynik, wybrana = transponowanie()
    if wynik:
        if wybrana == 'A':
            wyswietlanie(A,'Macierz A')
        else:
            wyswietlanie(B, 'Macierz B')
        wyswietlanie(wynik, f'Macierz {wybrana} transponowana')