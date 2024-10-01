import sys

sys.setrecursionlimit(10**9)


def calc_resto(n, resto, valori, monete, index):
    if n == 0:
        print(monete)
    else:
        if valori[index] > n:
            calc_resto(n, resto, valori, monete, index-1)
        else:
            monete += 1
            n -= valori[index]
            resto[index] += 1
            calc_resto(n, resto, valori, monete, index)
        

n = int(input())
valori = [1,2,5,10,20,50,100,200,500,1000]

for _ in range(n):
    resto = [0 for _ in range(10)]
    val = int(input())
    calc_resto(val, resto, valori, 0, len(resto) - 1)
    print(" ".join(str(x) for x in resto))