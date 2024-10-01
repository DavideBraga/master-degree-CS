import sys

sys.setrecursionlimit(10**9)

def arcobaleno(istanza, lenght):

    if len(istanza) == 0:
        return 0
    
    if len(istanza) == 1:
        return 1

    colore = istanza[0]
    index = 1

    while index < lenght:
        if colore == istanza[index]:
            return 1 + arcobaleno(istanza[1:index], len(istanza[1:index])) + arcobaleno(istanza[index:], len(istanza[index:])) - 1
        index += 1
    
    return 1 + arcobaleno(istanza[1:], len(istanza[1:]))


lenght = int(input())

array = list(map(int, input().strip().split()))

print(arcobaleno(array, lenght))