#!/usr/bin/python
n=3


def f(n):
    """ritorna il numero di piastrellature di un bagno 1xn"""
    assert n >= 0
    if n <= 1:
       return 1
    return f(n-1) + f(n-2)

def stampaPiastrellature(n, history=""):
    """stampa le piastrellature di un bagno 1xn, ciascuna prefissata dalla sua history
       Esempio n=3, history="":
          [][][]
          [--][]
          [][--]"""
    
    assert n >= 0
    if n == 0:
       print(history+"")
    elif n == 1:
       print(history+"[]")
    else:
       stampaPiastrellature(n-1, history+"[]")
       stampaPiastrellature(n-2, history+"[--]")




def f_intagliabili(n):
    assert n >= 0
    if n == 0:
        return 1
    elif n == 2:
        return 3
    return 2

def f(n):
    assert n >= 0
    if n == 1:
        return 2
    risp = f_intagliabili(n)
    for primo_taglio in range(1,n):
        risp += f_intagliabili(primo_taglio) * f(n - primo_taglio)
    return risp

n=int(input("N="))
print(f(n))
stampaPiastrellature(n)