def subseqcres(array):
    res = [1 for _ in range(len(array))]
    pel = [1 for _ in range(len(array))]
    for i in range((len(array) - 1), -1, -1):
        for j in range (i, len(array), 1):
            if array[j] > array[i]:
                res[i] = max(res[i], res[j] + 1)
                
    for i in range(len(array)):
        for j in range(i):
            if array[j] < array[i]:
                pel[i] = max(pel[i], pel[j] + 1)
        
    for i in range(len(array)):
        pel[i] += res[i] - 1

    return pel

n = int(input())

for _ in range(n):
    lenght = int(input())
    array = list(map(int, input().strip().split()))
    sol = subseqcres(array)
    print(" ".join(str(x) for x in sol))
