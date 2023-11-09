import math
def main():
    pass

#1)
def entfernen(list):
    nicht_entf = []
    s = []
    for ch in list:
        if ch not in s:             #in s care incepe gol se audauga pe rand fiecare element care nu se repeta
            nicht_entf.append(ch)
            s.append(ch)
    return nicht_entf

def test_entfernen():
    assert entfernen([43, 56, 72, 43, 56, 98, 50]) == [43, 56, 72, 98, 50]
    assert entfernen([43, 43, 43, 53, 63]) == [43, 53, 63]

# main()
# test_entfernen()

#2)
def paaren(list):
    umkehrungen = []
    ct = 0
    for ch1 in range(0, len(list)):
        u = 10*(list[ch1]%10) + int((list[ch1]/10))
        umkehrungen.append(u)                           #sortez lista initiala descrescator
        u = 0
    for ch2 in range(0, len(list)):
        if (list[ch2]) in umkehrungen:                  #verific daca exista perechi
            ct += 1
    return ct//2                                        #verificarea ia de 2 ori fiecare pereche

def test_paaren():
    assert paaren([48, 84, 92, 29, 43, 31]) == 2

# main()
# test_paaren()

#3)
def konkatenation(list):
    sortiert1 = sorted(list)[::-1]                      #sorteaza descrescator lista
    sortiert2 = [str(ch) for ch in sortiert1]           #transforma elementele listei in stringuri
    konk = int("".join(sortiert2))                      #concateneaza fiecare element si creeaza un numar
    return konk

def test_konkatenation():
    assert konkatenation([99, 88, 77, 66]) == 99887766
    assert konkatenation([98, 23, 86, 54]) == 98865423

# main()
# test_konkatenation()

#4)
def encrypt(list):
    encrypted = []
    for ch in range(0, len(list)):
        encrypted.append(list[ch] + list[0])            #adauga la fiecare element pe primul
    return encrypted

def test_encrypt():
    assert encrypt([11, 55, 66, 88, 99]) == [22, 66, 77, 99, 110]

# main()
# test_encrypt()

#5)
def filtr(list):
    gefiltert = []
    for ch in range(0, len(list)):
        if (list[ch]%10)/2 == int(list[ch]/10):         #adauga intr o noua lista fiecare element al carui
            gefiltert.append(list[ch])                  #cifra a zecilor e jumatate din cifra unitatilor
    return gefiltert

def test_filtr():
    assert filtr([12, 48, 85, 92, 36, 34]) == [12, 48, 36]

# main()
# test_filtr()

#6)
def domino_teilf(list):
    crt_subseq = [list[0]]
    max_subseq = [list[0]]
    for ch in range(1, len(list)):
        crt_num = list[ch]
        prev_num = list[ch - 1]
        if prev_num%10 == int(crt_num/10):          #verifica daca cifra unitatilor unui element este egala
            crt_subseq.append(list[ch])             #cu cifra zecilor urmatorului si le pune intr o noua lista
        else:
            crt_subseq = [list[ch]]
        if len(crt_subseq) >= len(max_subseq):
            max_subseq = crt_subseq
    return max_subseq

def test_domino_teilf():
    assert domino_teilf([21, 11, 17, 72, 98, 86, 61, 81]) == [21, 11, 17, 72]
    assert domino_teilf([51, 43, 12, 27]) == [12, 27]

# main()
# test_domino_teilf()

#7)
def kgV(list, frm, to):
    kgv = 1
    for ch in range(frm - 1, to):
        kgv = (kgv * list[ch]) // math.gcd(kgv, list[ch])           #iau unul cate unul elementele de la si
    return kgv                                                      #pana la pozitiile date, si fac pe rand
                                                                    #cmmmc folosind cmmdc
def test_kgV():
    assert kgV([20, 40, 12, 30, 11], 2, 4) == 120
    assert kgV([12, 24, 48, 11, 34, 52, 90, 71, 30], 1, 3) == 48

main()
test_kgV()