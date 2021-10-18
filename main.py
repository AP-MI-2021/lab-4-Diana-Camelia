def printMain():
    print("1. Citire lista. ")
    print("2. Stergere numere prime din lista. ")
    print("3. Verifica daca media aritmetica a numerelor din lista este mai mare decat un numar dat de la tastatura. ")
    print("4. Afisarea dupa fiecare element a numarului de divizori proprii.")
    print("x. Iesire. ")

"""
1. Citirea unei liste de numere intregi.
"""

def citire_lista():
    l = []
    n = int(input(" Dati numar de elemente: "))
    for i in range(n):
        l.append(int(input(i)))
    return l

"""
2. Afisarea listei dupa stergerea elementelor prime din lista.
"""

def isPrime(x):
    """
    Verifica daca un numar este prim.
    :param x: Un numar intreg
    :return: True, daca numarul e prim, respectiv, False, in caz contrar.
    """
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
    assert isPrime(2) is True
    assert isPrime(0) is False
    assert isPrime(3) is True
    assert isPrime(4) is False

def eliminare_numere_prime(l):
    """
    Sterge numere prime din lista.
    :param l: Lista de numere.
    :return: Lista fara numerele prime.
    """
    c_l = []
    for i in l:
        if isPrime(i) is False:
            c_l.append(i)
    return c_l

def test_eliminare_numere_prime():
    assert eliminare_numere_prime([8, 9, 17, 25]) == [8, 9, 25]
    assert eliminare_numere_prime([9, 8, 7, 6, 1, 2]) == [9, 8, 6, 1]
    assert eliminare_numere_prime([]) == []

def media_aritmetica(l):
    s = 0
    x = int(input("Dati un numar: "))
    a = len(l)
    for i in range(a):
        s = s + l[i]
    s = s // a
    if s > x:
        print("DA")
    else:
        print("NU")
    return

"""
4. Afisarea dupa fiecare element a numarului de divizori proprii.
"""

def nr_de_divizori(l):
    """
    Afiseaza dupa fiecare element numarul de divizori proprii.
    :param l: Lista de numere
    :return: Lista, unde, dupa fiecare element se afla numarul sau de divizori.
    """
    nr = 0
    c_l = []
    for i in l:
        c_l.append(i)
        nr = 0
        for j in range(1, i):
            if i % j == 0:
                nr = nr + 1
        c_l.append(nr)
    return c_l

def test_nr_de_divizori():
    assert nr_de_divizori([2, 4, 5, 6]) == [2, 1, 4, 2, 5, 1, 6, 3]
    assert nr_de_divizori([12, 34, 10]) == [12, 5, 34, 3, 10, 3]

def main():
    test_isPrime()
    test_eliminare_numere_prime()
    printMain()
    l = []
    while True:
        optiune = input("Dati o optiune: ")
        if optiune == "1":
            l = citire_lista()
        elif optiune == "2":
            print(eliminare_numere_prime(l))
        elif optiune == "3":
            media_aritmetica(l)
        elif optiune == "4":
            print(nr_de_divizori(l))
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati! ")

main()