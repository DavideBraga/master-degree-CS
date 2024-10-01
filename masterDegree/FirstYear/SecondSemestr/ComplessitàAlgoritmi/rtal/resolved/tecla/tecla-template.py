#!/usr/bin/env python3
from sys import stderr, stdout, argv


def solve(): # ToDo: decide the black-box contract (the arguments of this function and what it should return) 
    # TODO: write here your solution! (fullfill the contract)
    # what follows will be just good enough to respect the intended communication protocol with the server
    return [0]

              
if __name__ == "__main__":
    debug_level = 0
    if len(argv) == 2:
        debug_level = int(argv[1])
    T = int(input())
    for t in range(1, 1 + T):
        if debug_level > 0:
            print(f"#\n# Testcase {t}:", file=stderr)
        n, m = map(int, input().strip().split())
        for _ in range(m):
            a, b = map(int, input().strip().split())
            if debug_level > 1:
                print(f"# {a=}, {b=}", file=stderr)
             # ToDo: decide how to organize the data
        if debug_level > 1:
            print(f"# {n=}, {m=}", file=stderr)
        solution_path = solve() # ToDo: decide what arguments to pass
        L = len(solution_path)-1
        if debug_level > 2:
            print(f"# {L=}\n# {solution_path=}", flush=True, file=stderr)
        print(L)
        print(" ".join(map(str,solution_path)))
