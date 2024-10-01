#!/usr/bin/env python3
from sys import stderr, stdout, argv

import gurobipy as gp
from gurobipy import GRB


usage = f"""
   Call as follows:
      {argv[0]} [ debug_level ]

   where the 2 optional argument is:
   - debug_level
        0 print no debug info on stderr
        1 print checkpoint testcase number to help debugging
        2 print also the received instance
        3 echo on stderr also the output on stdout
        4 print also most significant internal data exchanges
        5 print also what Gurobi would say by default"""


INFEASIBLE = 3
FEASIBLE_AND_BOUNDED = 2

def model_and_compute_distances_with_gurobi(): # ToDo: decide the black-box contract (the arguments of this function and what it should return)
  with gp.Env(empty=True) as env:
    env.setParam('OutputFlag', 0)
    env.start()
    m = gp.Model(env=env)
    if debug_level < 5:
        m.Params.LogToConsole = 0
    # TODO: create variables. For the method addVars see the official documentation at https://www.gurobi.com/documentation/current/refman/py_model_addvars.html 
    m.update()
    # TODO: add constraints
    # TODO: Set objective function
    m.optimize()
    if debug_level > 3:
        print(m.Status)
    assert m.Status==FEASIBLE_AND_BOUNDED        
    # TODO: read out and format the optimal solution computed by gurobi. For the method getObjective and the methods of an Objective object see the official documentation at https://www.gurobi.com/documentation/current/refman/py_model_getobjective.html
    
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
