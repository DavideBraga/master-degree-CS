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

lista = parentesi(4)
for a in lista:
    print(a)