'''
Tecla implementato dalle matricole VR504272 e VR504230
'''

from collections import deque

def esplora_grafo():
    
    fifo = deque([(0, [])])

    flag = True

    while fifo:
        nodo, cammino = fifo.popleft()
        lenght = len(cammino)

        if nodo == 0 and (lenght % 2) != 0:
            print(lenght)
            print(" ".join(map(str, [0] + cammino)))
            flag = False
            break

        for v in grafo[nodo]:
            if (lenght + 1) % 2 == 0:
                if v not in open_bleah:
                    open_bleah.add(v)
                    fifo.append((v, cammino + [v]))
            else:
                if v not in open_slurp:
                    open_slurp.add(v)
                    fifo.append((v, cammino + [v]))
        
    if flag:
        print(0)
        print(0)


num_test = int(input().strip())

for _ in range(num_test):
    n, m = map(int, input().strip().split())
    grafo = [[] for _ in range(n)]
    open_bleah = set()
    open_slurp = set()
    path = []

    for _ in range(m):
        u, v = map(int, input().strip().split())
        grafo[u].append(v)
        grafo[v].append(u)
    
    open_bleah.add(0)
    esplora_grafo()