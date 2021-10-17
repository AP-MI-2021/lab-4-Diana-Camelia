"""
Scrieți un program cu meniu (meniul va conține o opțiune care oprește programul) care suportă operațiile:

1. [1p] Citirea unei liste de float-uri. Citirile repetate suprascriu listele precedente.
2. [2p] Afișarea tuturor numerelor întregi din listă (de exemplu, 3 și 2.0 se consideră întregi).
3. [2p] Afișarea celui mai mare număr divizibil cu un număr citit de la tastatură.
4. [2p] Afișarea tuturor float-urilor ale căror parte fracționară este palindrom.
5. [3p] Afișarea listei obținute din lista inițială în care float-urile cu partea întreagă a radicalului număr
    prim sunt puse ca string-uri cu caracterele în ordine inversă.
    Exemplu: [10.0, 100.0, 12.45, 50.0, 101.2] --> ['0.01', 100.0, '54.21', '0.05', 101.2]
"""

def printMenu():
    print("1. Citire lista de float-uri. ")
    print("2. Afișarea tuturor numerelor întregi din listă. ")
    print("3. Afișarea celui mai mare număr divizibil cu un număr citit de la tastatură. ")
    print("4. Afișarea tuturor float-urilor ale căror parte fracționară este palindrom. ")
    print("5. Afisarea listei, unde, numerele care au radicalul partii intregi un numar prim vor fi scrise ca string-uri cu caracterele în ordine inversă.")
    print("x. Iesire. ")

def citire_lista_float():
    l = []
    n = int(input("Dati numar de elemente: "))
    for i in range(n):
        l.append(float(input("l[" + str(i) + "] = ")))
    return l

""" 2. Afișarea tuturor numerelor întregi din listă (de exemplu, 3 și 2.0 se consideră întregi). """

def numere_intregi(l):
    """
    Verifica care numere din lista sunt numere intregi (de tip int).
    :param l: Lista de float-uri
    :return: O subsecventa ce contine numerele intrgi ale listei date.
    """
    l_intregi = []
    for i in range(len(l)):
        if int(l[i]) == l[i]:
            l_intregi.append(l[i])
    return l_intregi

def test_numere_intregi():
    assert numere_intregi([10.0, 100.0, 12.45, 50.0, 101.2]) == [10.0, 100.0, 50.0]
    assert numere_intregi([10.45, 3.06, 8.0, 3.02, 0.19]) == [8.0]
    assert numere_intregi([]) == []
    assert numere_intregi([2.09, 10.10, 90.80]) == []
    assert numere_intregi([2.0, 2.1]) == [2.0]

""" 3. Afișarea celui mai mare număr divizibil cu un număr citit de la tastatură. """

def cmm_nr_diviz_cu_k(l):
    """
    Aflarea celui mai mare număr divizibil cu un număr citit, de la tastatura, prin parametrul k.
    :param l: Lista de float-uri
    :return: Cel mai mare număr divizibil cu un număr citit, de la tastatura, prin parametrul k.
    """
    k = int(input("Dati un numar: "))
    maxim_numar = 0
    for i in range(len(l)):
        if l[i] % k == 0 and maxim_numar < l[i]:
            maxim_numar = l[i]
    return maxim_numar

""" 4. Afișarea tuturor float-urilor ale căror parte fracționară este palindrom. """

def is_palindrome(n):
    """
    Determina daca un numar dat este palindrom
    :param n: numar intreg
    :return: True, daca numarul dat este palindrom, respectiv False, in caz contrar.
    """
    x = int(n)
    k = 0
    while x > 0:
        k = k * 10 + x % 10
        x = x // 10
    if k == n:
        return True
    else:
        return False

def test_is_palindrome():
    assert is_palindrome(123) is False
    assert is_palindrome(12321) is True
    assert is_palindrome(12) is False
    assert is_palindrome(6789876) is True
    assert is_palindrome(987789) is True

def numar_intreg(x):
    """
    Verifica daca un numar este intreg sau nu.
    :param x: Un numar float sau int.
    :return: True, daca numarul este intreg, respectiv, False, in caz contrar.
    """
    if x == int(x):
        return True
    return False

def palindrom_parte_fractionara(l):
    list = []
    for i in l:
        if numar_intreg(i) == False:
            i = str(i)
            value = i.split('.')[1]
            if value == value[::-1]:
                list.append(float(i))
    return list

def test_palindrom_parte_fractionara():
    assert palindrom_parte_fractionara([12.121, 10.01, 8.0, 19.6, 0.717]) == [12.121, 19.6, 0.717]
    assert palindrom_parte_fractionara([12.0, 1.09, 7.9, 10.01]) == [7.9]
    assert palindrom_parte_fractionara([]) == []

"""5. Afișarea listei obținute din lista inițială în care float-urile cu partea întreagă a radicalului număr
    prim sunt puse ca string-uri cu caracterele în ordine inversă.
    Exemplu: [10.0, 100.0, 12.45, 50.0, 101.2] --> ['0.01', 100.0, '54.21', '0.05', 101.2]"""

def isPrime(x):
    '''
    Determina daca un numar este prim
    :param x: un numar intreg
    :return: True, daca x este prim si False, in caz contrar
    '''
    ok = True
    if x < 2:
        return False
    for i in range(2, x // 2 + 1):
        if x % i == 0 and ok == True:
            ok = False
    if ok:
        return True
    else:
        return False

def test_isPrime():
    assert isPrime(-1) is False
    assert isPrime(0) is False
    assert isPrime(1) is False
    assert isPrime(2) is True
    assert isPrime(3) is True
    assert isPrime(4) is False
    assert isPrime(5) is True

def radical_cu_parte_intreaga(l):
    """
    Determinarea listei obținute din lista inițială în care float-urile cu partea întreagă a radicalului număr
    prim sunt puse ca string-uri cu caracterele în ordine inversă.
    :param l: Lista de float-uri
    :return: Lista în care float-urile cu partea întreagă a radicalului număr prim sunt puse ca string-uri cu
    caracterele în ordine inversă.
    """
    list = []
    for i in l:
        radique = int(i ** 0.5)
        if isPrime(radique) == True:
            i = str(i)[::-1]  # introducem caracterele in ordine inversa
            list.append(i)
        else:
            list.append((i))
    return list

def test_radical_cu_parte_intreaga():
    assert radical_cu_parte_intreaga([10.0, 100.0, 12.45, 50.0, 101.2]) == ['0.01', 100.0, '54.21', '0.05', 101.2]
    assert radical_cu_parte_intreaga([20.0, 11.11, 9.123, 8.7, 21.35]) == [20.0, '11.11', '321.9', '7.8', 21.35]
    assert ([]) == []
    assert ([109.0, 100.0]) == [109.0, 100.0]

def main():
    test_numere_intregi()
    test_is_palindrome()
    test_palindrom_parte_fractionara()
    test_isPrime()
    test_radical_cu_parte_intreaga()
    printMenu()
    l = []
    while True:
        optiune = input("Dati optiunea: ")
        if optiune == "1":
            l = citire_lista_float()
        elif optiune == "2":
            print(numere_intregi(l))
        elif optiune == "3":
            print(cmm_nr_diviz_cu_k(l))
        elif optiune == "4":
            print(palindrom_parte_fractionara(l))
        elif optiune == "5":
            print(radical_cu_parte_intreaga(l))
        elif optiune == "x":
            break
        else:
            print(" Optiune gresita! Reincercati! ")
main()