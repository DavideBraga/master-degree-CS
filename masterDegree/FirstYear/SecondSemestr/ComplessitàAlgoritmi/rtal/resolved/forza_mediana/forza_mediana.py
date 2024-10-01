#!/usr/bin/env python3
import sys

'''Forza mediana implementa dalle matricole VR504272 e VR504230'''

def ask_oracolo(a, b, c):
    ''' CHiedo all'oracolo la mediana'''
    print(a, b, c)
    sys.stdout.flush()
    return int(input().strip())

def ricerca(x, s, d, ord):
    '''Funzione che fa la ricerca ternaria per trovare la posizione di x nell'array ord'''
    s3 = s + (d - s) // 3
    d3 = s + (2 * (d - s) + 1) // 3

    if s == d:
        if s:
            s -= 1
        else:
            d += 1

    if d == s + 1:
        t = ask_oracolo(ord[s], ord[d], x)
        if t == x:
            return d
        elif t == ord[s]:
            return s
        else:
            return d + 1

    t = ask_oracolo(ord[s3], ord[d3], x)

    if t == x:
        if s3 + 1 == d3:
            return d3
        return ricerca(x, s3 + 1, d3 - 1, ord)

    if t == ord[s3]:
        if s == s3:
            return s
        return ricerca(x, s, s3 - 1, ord)

    if d3 == d:
        return d + 1
    return ricerca(x, d3 + 1, d, ord)

def processa_istanza(n):
    # chiedo all'oracolo la mediana tra i primi 3 numeri
    i = ask_oracolo(0, 1, 2)

    ord = [0] * n
    if i == 0:
        ord[0], ord[1], ord[2] = 1, 0, 2
    elif i == 1:
        ord[0], ord[1], ord[2] = 0, 1, 2
    else:
        ord[0], ord[1], ord[2] = 0, 2, 1

    # per i numeri da 3 a n cerco di ordinarli chiamando la funzione ricerca
    l = 3
    for i in range(3, n):
        if i > (n + 1) // 2 + 1:
            ord = ord[1:l]
            l -= 2

        if l == 1:
            break

        t = ricerca(i, 0, l - 1, ord)

        # costruisco ord eliminando gli elementi che non possono essere la mediana
        ord = ord[:t] + [i] + ord[t:l]
        l += 1

    print(ord[l // 2])
    sys.stdout.flush()


def main():
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())

        if n >= 3:
            processa_istanza(n)
        else:
            print(0)
            sys.stdout.flush()

if __name__ == "__main__":
    main()