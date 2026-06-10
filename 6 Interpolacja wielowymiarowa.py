#Dane Testowe
x_punkty = [1.0, 2.0, 4.0, 5.0, 7.0]
y_punkty = [2.0, 4.5, 1.5, 5.0, 3.0]

wybor = int(input('Którą Interpolacje wybierasz?\n1 -> Interpolacja Lagrange’a\n2 -> Interpolacja funkcjami sklejanymi trzeciego stopnia z algorytmem Thomasa\n'))

n = len(x_punkty)

#Interpolacja Lagrange'a
if wybor == 1:

    print('Interpolacja Lagrange’a dla punktów\nx = ',x_punkty,'\ny = ',y_punkty)

    #Pusta lista na wynik
    A = [0] * n

    for i in range(n):
        w = [1] #wielomian
        M = 1 #mianownik we wzoru Lagrange'a 

        for j in range(n):

        
            if j!=i: #warunek Lagrange'a
                mnozenie = [0] * (len(w) + 1) #do przetrzymania wielomianu

                #mnożenie wielomianu przez czynnik (x - x_j)
                for k in range(len(w)):
                    mnozenie[k] += -x_punkty[j] * w[k]
                    mnozenie [k + 1] += w[k]
            
                w = mnozenie

                #Mianownik wzoru Lagrange'a (x_i - x_j)
                M *= (x_punkty[i] - x_punkty[j])
        
        #Zapis wielomianu
        for k in range(len(w)):
            A[k] += y_punkty[i] * w[k] / M

    print('\nWspółczynniki wyznaczonego wielomianu:\n',A)


#Interpolacja funkcjami sklejanymi trzeciego stopnia z algorytmem Thomasa
elif wybor == 2:

    print('Interpolacja funkcjami sklejanymi trzeciego stopnia z algorytmem Thomasa\nx = ',x_punkty,'\ny = ',y_punkty)

    #Długości przedziałów
    p = []

    for i in range(n-1):
        p.append(x_punkty[i+1] - x_punkty[i])

    #Budowa układu trójdiagonalnego
    a = [0] * n     #współczynniki pod przekątną
    b = [0] * n     #przekątna główna
    c = [0] * n     #nad przekątną
    d = [0] * n     #prawa strona

    #Pierwsze i ostatnie równanie
    b[0] = 1
    b[n-1] = 1

    for i in range(1, n-1):

        #budowanie układu 
        a[i] = p[i-1]

        b[i] = 2 * (p[i-1] + p[i])

        c[i] = p[i]

        d[i] = 6 * ((y_punkty[i+1] - y_punkty[i]) / p[i] - (y_punkty[i] - y_punkty[i-1]) / p[i-1])

    #Algorytm Thomasa

    #1 Eliminacja do przoodu
    cn = [0] * n    #nowe współczynniki nad przekątną
    dn = [0] * n    #nowe prawe strony

    #Pierwszy wiersz
    cn[0] = c[0] / b[0]
    dn[0] = d[0] / b[0]

    #Pętla eliminacji do przodu
    for i in range(1, n):

        mianownik = b[i] - a[i] * cn[i-1]

        cn[i] = c[i] / mianownik

        dn[i] = (d[i] - a[i] * dn[i-1]) / mianownik

    #2 Podstawianie wstecz
    M = [0] * n

    M[n-1] = dn[n-1]

    for i in range(n-2, -1, -1):

        M[i] = dn[i] - cn[i] * M[i+1]

    #Miejsce na współczynniki splajnów
    A = []
    B = []
    C = []
    D = []

    for i in range(n-1):

        A.append(y_punkty[i])

        B.append((y_punkty[i+1] - y_punkty[i]) / p[i] - p[i] * (2*M[i] + M[i+1]) / 6)

        C.append(M[i] / 2)

        D.append((M[i+1] - M[i]) / (6*p[i]))

    print('\nWspółczynniki spline:\nA = ',A,'\nB = ', B,'\nC = ', C,'\nD = ', D)

