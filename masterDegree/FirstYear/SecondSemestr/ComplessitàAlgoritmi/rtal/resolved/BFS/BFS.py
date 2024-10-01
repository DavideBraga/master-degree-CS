import sys

n = int(input()) 

for _ in range(n):
    val = input().split()
    num_nodi = int(val[0])
    num_archi = int(val[1])
    fifo = []
    tot = 1
    arco = [[] for _ in range(num_nodi)]
    dis = [None for _ in range(num_nodi)]
    papi = ["" for _ in range(num_nodi)]
    papis = [[] for _ in range(num_nodi)]
    
    for _ in range(num_archi):
        line = input().split(" ")
        k = int(line[0])
        h = int(line[1])
        arco[k].append(h)

    dis[0] = 0
    papi[0] = 0
    papis[0].append(0)
    fifo.append(0)
    while len(fifo) != 0:
        value = fifo[0]
        fifo = fifo[1:]
        for z in arco[int(value)]:
            papis[int(z)].append(value) 
            if dis[int(z)] == None:
                dis[int(z)] = dis[int(value)] + 1
                papi[int(z)] = value
                fifo.append(z)

    for i in range(num_nodi):
        sub = 1
        for j in papis[i]:
            if dis[j] == dis[papi[i]] and (j != papi[i]):
                sub += 1
        tot *= sub    


    print(" ".join(str(x) for x in dis))
    print(" ".join(str(x) for x in papi))
    print((tot) % 1000000007)



    