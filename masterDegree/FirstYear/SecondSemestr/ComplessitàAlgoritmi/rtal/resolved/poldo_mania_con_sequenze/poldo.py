test = int(input())

#soluzione con gtp un po'strana

for _ in range(test) :
    n = int(input())
    S = list(map(int, input().strip().split()))

    res = [0 for _ in range(n)]
    percorso = [-1 for _ in range(n)]

    max_index = 0
    max_val = res[0]

    indexes = []

    for i in range(n):
        res[i] = S[i]

    for i in range(1,n):
        for j in range(i):
            if S[j] < S[i] and (i-j) > 0:
                if res[j] + S[i] > res[i]:
                    res[i] = res[j] + S[i]
                    percorso[i] = j

    for i in range(1,n):
        if res[i] > max_val:
            max_val = res[i]
            max_index = i

    
    while max_index != -1:
        indexes.append(max_index)
        max_index = percorso[max_index]

    indexes = indexes[::-1]

    print(*indexes)
