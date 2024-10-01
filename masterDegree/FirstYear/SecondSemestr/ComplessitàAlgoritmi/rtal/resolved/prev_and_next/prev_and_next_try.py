# le funzioni parentesi_succ e parentesi_prev sono state scritte insieme a Matteo Vesentini, matricola VR508279

import sys

sys.setrecursionlimit(10**9)
ending_sequence = []
beginning_sequence = []
conf = ""

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

def parentesi_prev(req):
    length = len(req)
    index = length - 1
    prev = req[:]

    #parentesizzazione sempre precedenti
    if req == "()" * (length//2):
        return ""

    if req == "":
        return ""
    parentesi_aperte = 0
    parentesi_chiuse = 0

    #identifico la sottoparentesizzazione più a destra
    while index >= 0:
        if prev[index] == ')':
            parentesi_chiuse += 1
        else:
            parentesi_aperte += 1

        if parentesi_aperte == parentesi_chiuse:
            break

        index -= 1

    right = prev[index : length]

    parentesi_aperte = 0
    parentesi_chiuse = 0
    bound = index   #divisore tra la parte sinistra e destra
    index = index -1
    cont = True
    #il ciclo con cont mi permette di accorpare i () adiacenti a destra in una unica stringa
    while cont:
        while index >= 0:
                if prev[index] == ')':
                    parentesi_chiuse += 1
                else:
                    parentesi_aperte += 1

                if parentesi_aperte == parentesi_chiuse:
                    break

                index -= 1

        left = prev[index: bound]

        if left == "()" and right == "()" * (len(right) // 2):
            right = left + right
            parentesi_aperte = 0
            parentesi_chiuse = 0
            index = index-1
            left = ""
            bound = bound - 2
        else:
            cont = False
    
    if right in beginning_sequence:    #se la parte destra è una sequenza terminale
        num_parentesi_interne = (len(right) // 2) - 1
        len_restante = length - len(prev[:bound]) - len(right) + 2
        return  prev[:bound] + '(' * num_parentesi_interne + ')' * num_parentesi_interne + '(' * (len_restante//2) + ')' * (len_restante//2)
    else:
        if left in beginning_sequence:
            if right == "()" * (len(right) // 2):
                parentesi_interne = (len(left) // 2) - 1
                parentesi_totali = parentesi_interne + 1 + (len(right) // 2)
                return prev[:index] + '(' * parentesi_interne + ')' * parentesi_interne + '(' * (parentesi_totali - parentesi_interne) + ')' * (parentesi_totali - parentesi_interne)
            else:
                return prev[:bound] + '(' + parentesi_prev(right[1:-1]) + ')'
        else:
            if right == "()" * (len(right) // 2):
                return prev[:index] + '(' + parentesi_prev(left[1:-1]) + ')' + '(' * (len(right) // 2) + ')' * (len(right) // 2)
            else:
                return prev[:bound] + '(' + parentesi_prev(right[1:-1]) + ')'


def parentesi_succ(req):
    length = len(req)
    index = length - 1
    succ = req[:]

    if req == "":
        return ""

    if succ == ending_sequence[-1]:
        return ""

    parentesi_aperte = 0
    parentesi_chiuse = 0

    while index >= 0:
        if succ[index] == ')':
            parentesi_chiuse += 1
        else:
            parentesi_aperte += 1

        if parentesi_aperte == parentesi_chiuse:
            break

        index -= 1

    right = succ[index : length]

    parentesi_aperte = 0
    parentesi_chiuse = 0
    bound = index
    index = index -1

    while index >= 0:
        if succ[index] == ')':
            parentesi_chiuse += 1
        else:
            parentesi_aperte += 1

        if parentesi_aperte == parentesi_chiuse:
            break

        index -= 1

    left = succ[index: bound]

    if right not in ending_sequence:
        return succ[:bound] + '(' + parentesi_succ(right[1:-1]) + ')'
    else:
        if left in ending_sequence:
            size = int(len(left)/2)
            tmp = ""
            for _ in range(size):
                tmp += "()"
            tmp = succ[:index] + "(" + tmp +")"
            while len(tmp) < length:
                tmp += "()"
            return tmp
        else:
            tmp = succ[:index] + '(' + parentesi_succ(left[1:-1]) + ')'
            while len(tmp) < length:
                tmp += "()"
            return tmp

    

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
        s = ""
        for _ in range(int(len(req)/2)):
            s = "(" + s + ")"
            ending_sequence.append(s)
        s = ""
        temp = []
        for _ in range(int(len(req)/2) - 1):
            s += "()"
            temp.append(s)
        beginning_sequence = ['(' + x + ')' for x in temp]
        print(parentesi_prev(req))
        print(parentesi_succ(req))
         
    else:
        numeri(req)
