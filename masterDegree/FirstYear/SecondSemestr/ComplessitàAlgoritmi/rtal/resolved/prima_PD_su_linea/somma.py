#!/usr/bin/python
A = list(map(int, input().strip().split()))
n = len(A)
opt_val = [None for _ in range(n)]

def f(i):
    return 0 if i < 0 else opt_val[i]

for i in range(n):
    opt_val[i] = max(f(i-1), A[i-1] + f(i-4) )
print(opt_val[n-1])

exit(0)