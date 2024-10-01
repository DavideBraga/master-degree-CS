test = int(input())  

for _ in range(test):

    m, n = list(map(int, input().split()))
    
    if(m == n):
        start = 2
    else:
        start = 1
        
    print(start)

    while True:
        if(start == 1):
            size = min(m, n)
            m = size
            n = size
            print(size, size)
            
            if n == 1 and m == 1:
                break
            m, n = list(map(int, input().strip().split()))
            
            if n == 1 and m == 1:
                break
        else:
            m, n = list(map(int, input().strip().split()))
            
            if n == 1 and m == 1:
                break
            
            size = min(m, n)
            m = size
            n = size
            print(size, size)
            
            if n == 1 and m == 1:
                break
