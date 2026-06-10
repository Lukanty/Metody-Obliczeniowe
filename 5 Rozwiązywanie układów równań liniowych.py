print('Układ równań który będzie rozwiązywany:\n2 - 2y + z = -3\nx + 3y - 2z = 1\n3x - y - z =2\n')

A = [[2, -2, 1], [1, 3, -2], [3, -1, -1]]

B = [[-3],[1],[2]]

#1 Macierz rozszerzona
n = len(A)
for i in range(n):
    A[i].append(B[i][0])

print('Macierz rozszerzona')
#Wyświetlenie macierzy
for i in range(len(A)):
    print(A[i])

wybor = int(input('\nRozwiązywanie układów równań\n1 -> Metodą eliminacji Gaussa\n2 -> Metodą eliminacji Gaussa - Jordana\n'))


if wybor == 1:
    #2 Etap1 Eliminacja w przód 
    for i in range(n):
        
        #Wybór elementu osiowego
        element_osiowy = i
        max_abs = abs(A[i][i]) #maksymalna wartość bezwzgędna
        
        for j in range(i + 1, n):
            
            if abs(A[j][i]) > max_abs:
                max_abs = abs(A[j][i])
                element_osiowy = j
        
        #Zabezpieczenie przed nierozwiązalnym układem
        if max_abs == 0:
            print('Układ nieoznaczony, ma wiele rozwiązań')
            exit()
        
        #Zamiana wierszy
        if element_osiowy != i:
            A[i], A[element_osiowy] = A[element_osiowy], A[i]
        
        #Zerowanie wiersz
        for j in range(i + 1, n):
            ile_razy = A[j][i] / A[i][i]
            
            for k in range(i, n + 1):
                A[j][k] -= ile_razy * A[i][k]

    print("\nMacierz po eliminacji:")

    for wiersz in A:
        print(wiersz)


    #3 Etap2 Rozwiązywanie układu
    for i in range(n - 1, -1, -1):
        suma = 0
        
        for j in range(i + 1, n):
            suma += A[i][j] * A[j][n]

        A[i][n] = (A[i][n] - suma) / A[i][i]     

    print('\nRozwiązanie (x, y, z):\nx = ',A[0][n],'\ny = ',A[1][n],'\nz = ',A[2][n],'\n\nMacierz')

    #Wyświetlenie macierzy
    for i in range(len(A)):
        print(A[i])



elif wybor == 2:
    #2 Etap1 Eliminacja w przód 
    for i in range(n):
        
        #Wybór elementu osiowego
        elemant_osiowy = i
        max_abs = abs(A[i][i]) #maksymalna wartość bezwzgędna

        for j in range(i + 1, n):
            
            if abs(A[j][i]) > max_abs:
                max_abs = abs(A[j][i])
                elemant_osiowy = j

        #Zabezpieczenie przed nierozwiązalnym układem
        if max_abs == 0:
            print('Układ nieoznaczony, ma wiele rozwiązań')
            exit()
        
        #Zamaina wierszy
        if elemant_osiowy != i:
            A[i], A[elemant_osiowy] = A[elemant_osiowy], A[i]
        
        #Dzielimy wiersz prze element osiowy
        elemant_osiowy = A[i][i]
        for j in range(i, n + 1):
            A[i][j] /= elemant_osiowy
        
        #Zerowanie wierszy
        for j in range(n):
            
            if j != i:
                ile_razy = A[j][i]
                
                for k in range(i, n + 1):
                    A[j][k] -= ile_razy * A[i][k]

    print('\nRozwiązanie (x, y, z):\nx = ',A[0][n],'\ny = ',A[1][n],'\nz = ',A[2][n],'\n\nMacierz')
    
    #Wyświetlenie macierzy
    for i in range(len(A)):
        print(A[i])