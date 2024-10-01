#!/usr/bin/python
from sys import stdin, stdout, stderr

def dfs(v):
    global t, log
    if open[v] is not None:
        return
    open[v] = t; t += 1; log += f"({v}- "
    for z in out_nei[v]:
        dfs(z)
    close[v] = t; t += 1; log += f" -{v})"



n,m = map(int, input().strip().split())
V = list(range(n))
out_nei = [ [] for _ in V]
for _ in range(m):
    u,v = map(int, input().strip().split())
    out_nei[u].append(v)

print(f"{n=}\n{m=}\n{out_nei=}", file=stderr)
t = 0
open = [ None for _ in V]
close = [ None for _ in V]
#dad = [ None for _ in V]
log = ""
dfs(0)
print(f"    v={list(range(n))}\n {open=}\n{close=}\n{log=}", file=stderr)