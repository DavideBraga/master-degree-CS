import sys

sys.setrecursionlimit(10**9)

def piastrelle_succ(req):
    if "[]" not in req:
        return ""
    
    length = len(req)

    if length == 0:
        return ""
    
    succ = req[:]
    while length:
        #parto dal fondo e verifico
        #per n fino a 6 ho [][]--->[--]
        if succ[length - 4 : length] == "[][]":
            succ = succ[: length-4] + "[--]" + succ[length:]
            break
        if succ[length-4 : length] == "[--]":
            #per n fino a 6 ho [--][--]--->next(n-2)[--]
            if succ[length - 8 : length-4] == "[--]":
                succ = piastrelle_succ(req[: length-4]) + "[][]" + succ[length:]
                break
            #per n fino a 6 ho [][][--]--->[][--][]
            else:
                succ = succ[: length-6] + "[--][]" + succ[length:]
                break
        else:
            length -= 2

    if len(succ) != len(req):
        return ""
    return succ

def piastrelle_prev(req):
    if "[--]" not in req:
        return ""
    
    length = len(req)

    if length <= 0:
        return ""
    
    prev = req[:]

    while length != 0:
        #parto dal fondo e verifico
        #per n fino a 6 ho [--]--->[][]
        if prev[length-4 : length] == "[--]":
            prev = prev[: length-4] + "[][]" + prev[length:]
            break
        #per n fino a 6 ho [--][]--->[][--]
        if prev[length-6 : length] == "[--][]":
            prev = prev[: length-6] + "[][--]" + prev[length:]
            break
        #se ho [][] devo fare -> next(piastrelle(n-2)) + [][]
        else:
            if prev[length-8 : length] == "[--][][]":
                prev = prev[: length-8] + "[][--][]" + prev[length:]
                break
            else:
                prev = piastrelle_prev(req[: length-4]) + "[--]" + prev[length:]
                break

    if len(prev) != len(req):
        #print("sono qui")
        return ""

    return prev

def parentesi(n):
    if n >= 2:
        poss_par = [None for _ in range(n+1)]
        poss_par[0] = [""]
        poss_par[1] = ["()"]

    
        for i in range(2, n+1):
            poss_par[i] = []
            for j in range(i):
                for nested in poss_par[j]:
                    for right in poss_par[i-j-1]:
                        poss_par[i].append("(" + nested + ")" + right)

    return poss_par[n]

def numeri(req):
    values = list(map(int, req.split()))
    base = max(values) + 1
    dim = len(values)
    prev = values[:]
    succ = values[:]
    carry = False

    for i in range (dim-1, -1, -1):
        if prev[i] > 0:
            prev[i] -= 1
            carry = False
            break
        else:
            prev[i] = base - 1
            carry = True

    if carry:
        print()
    else:
        print(" ".join(map(str, prev)))

    carry = False

    for i in range (dim-1, -1, -1):
        if succ[i] < (base-1):
            succ[i] += 1
            carry = False
            break
        else:
            succ[i] = 0
            carry = True

    if carry:
        print()
    else:
        print(" ".join(map(str, succ)))
    
t = int(input())

for _ in range(t):

    req = input()

    if '[' in req:
        print(piastrelle_prev(req))
        print(piastrelle_succ(req))
    elif '(' in req:

        lista = parentesi(int(len(req)/2))
        
        for i, par in enumerate(lista):
            if par == req:
                if i > 1:
                    print(lista[i-1])
                else:
                    print()
                if i < len(lista)-1:
                    print(lista[i+1])
                else:
                    print()
        
    else:
        numeri(req)