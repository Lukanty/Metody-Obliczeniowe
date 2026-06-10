import math 

print('Program oblicza równanaie nieliniowe sin(x) = 0')

def f(x):
    return math.sin(x)

def pochodna(x):
    h = 0.0001
    return (f(x+h)-f(x-h))/(2*h)


wybor = int(input('Jaką metodą chcesz rozwiązać równanie nieliniowe?\n1 -> Metoda Bisekcji\n2 -> Metoda Newtona\n3 -> Metoda Siecznych\n'))

#funckcja -> sin(x)

#wybór
if wybor == 1:
    #Metoda Bisekcji
    #1

    zabezpieczenie = 0

    #Podbranie danych od użytkownika + spradzenie założenie
    while True:
        a = float(input('Podaj początek zakresu: ')) #a
        b = float(input('Podaj koniec zakresu: ')) #b
        dokladnosc = float(input ('Podaj dokładność: ')) #ε

        if f(a) * f(b) < 0:
            print('Przedział spełnia założenie')
            break
        else:
            print('Przedział nie spełnia założenia f(a)*f(b)<0, podaj nowy przedział')
        
        if zabezpieczenie >= 1000:
            print ('Przekroczono limit 1000')
            break

        zabezpieczenie += 1

    zabezpieczenie = 0

    #Algorytm Bisekcji
    while True:
        #2
        c = (a + b)/2 #środek przedziału
        #3
        if abs(f(c)) < dokladnosc: #abs to wartośc bezwzgędna
            print ('Rozwiązanie równania: ', c)
            print ('wykonano ', zabezpieczenie, ' iteracji')
            break
    
        else:
            #4
            if f(a) * f(c) < 0:
                b = c
            else:
                a = c

        if zabezpieczenie >= 1000:
            print ('Przekroczono limit 1000')
            break

        zabezpieczenie += 1

    print('Koniec pętli')
        
    
elif wybor == 2:
    #Metoda Newtona
    
    zabezpieczenie = 0

    #Podbranie danych od użytkownika + spradzenie założenie
    while True:
        #1
        x_0 = float(input('Podaj punkt startowy: ')) #punkt startowy
        dokładnosc_pkt = float(input('Podaj dokładność punktu: ')) #δ
        dokladnosc_f = float(input ('Podaj dokładność Funckji: ')) #ε

        if pochodna(x_0) != 0:
            break
        else:
            print('Punkt nie spełnia założenia pochodna f(x) jest różna od zera, podaj nowy punkt')

        if zabezpieczenie >= 1000:
            print ('Przekroczono limit 1000')
            break

        zabezpieczenie += 1

    zabezpieczenie = 0

    #Algorytm Newtona
    while True:
        #2
        x_n = x_0 - (f(x_0)/pochodna(x_0)) #x_1 to jest kolejny punkt
        #3
        if abs((x_n) - x_0) < dokładnosc_pkt or abs(f(x_n)) < dokladnosc_f:
            print ('Rozwiązanie równania: ', x_n)
            print ('wykonano ', zabezpieczenie, ' iteracji')
            break
        else:
            x_0 = x_n
        
        if zabezpieczenie >= 1000:
            print ('Przekroczono limit 1000')
            break

        zabezpieczenie += 1
    
    print('Koniec pętli')   

elif wybor == 3:
    #Metoda Siecznych

    zabezpieczenie = 0

    #Podbranie danych od użytkownika + spradzenie by x_0 i X_1 nie były tym samym
    while True:
        #1
        x_0 = float(input('Podaj pierwszy punkt startowy: ')) #pierwszy punkt startowy
        x_1 = float(input('Podaj drugi punkt startowy: ')) #drugi punkt startowy
        dokładnosc_pkt = float(input('Podaj dokładność punktu: ')) #δ
        dokladnosc_f = float(input ('Podaj dokładność Funckji: ')) #ε

        if x_0 != x_1:
            break
        else:
            print('x_0: ', x_0,'i x_1: ', x_1,'nie mogą mieć tych samych wartości')
        
        if zabezpieczenie >= 1000:
            print ('Przekroczono limit 1000')
            break
        
        zabezpieczenie += 1    
    
    zabezpieczenie = 0

    #Algorytm siecznej
    while True:
        #2
        x_n = x_1 - (f(x_1)*(x_1 - x_0))/(f(x_1) - f(x_0))

        #3
        if abs(x_n - x_1) < dokładnosc_pkt or abs(f(x_n)) < dokladnosc_f:
            print ('Rozwiązanie równania: ', x_n)
            print ('wykonano ', zabezpieczenie, ' iteracji')
            break
        else:
            x_0 = x_1
            x_1 = x_n

        if zabezpieczenie >= 1000:
            print ('Przekroczono limit 1000')
            break
        
        zabezpieczenie += 1

    print('Koniec pętli') 