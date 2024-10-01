#!/usr/bin/python
from sys import stderr

def listaSoluzioni(B, history = None):
    if history is None:
        history = [B]
    if B == 0:
        print(" ".join(map(str, history[1:])))
    else:
        print("son qua", history[-1])
        for first_prize in reversed(range(1, 1 + min(B, history[-1]))):
            listaSoluzioni(B - first_prize, history + [first_prize])

print("Inserisci il numero di tescases che intendi affrontare:", end = " ", file=stderr)
T = int(input())
for t in range(1, 1 + T):
    print(f"\nCase {t}:", file=stderr)
    n = int(input())
    listaSoluzioni(n)
