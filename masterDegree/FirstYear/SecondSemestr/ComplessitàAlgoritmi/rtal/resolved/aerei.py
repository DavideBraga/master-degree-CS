import sys

sys.setrecursionlimit(10**9)

def distanza_percorsa(n):
    if n == 0:
        return 0
    return (1/n) + distanza_percorsa(n-1)

def distanza_percorsa_iter(n):
    distanza = 0
    for i in range(1, n+1):
        distanza += 1/n
    return distanza

def num_aerei(n, distanza):
    if distanza <= 0:
        return n
    else:
        return num_aerei(n+1, distanza - (1/(n+1)))


def num_aerei_iter(n, distanza):
    while distanza > 0:
        n += 1
        distanza -= 1/(n+1)


n = int(input())
print(distanza_percorsa(n))
print(num_aerei(0, 5))