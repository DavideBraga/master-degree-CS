def ricercabinaria(left, right):
    while left <= right:
        if left == right:
            print(f"!{right}", flush=True)
            return
        guess = (left + right) // 2
        print(f"?{guess}", flush=True)
        resp = input()
        if resp == "=":
            print(f"!{right}", flush=True)
            return
        elif resp == "<":
            right = guess - 1
        else:
            left = guess + 1

def ricercabinaria_bugiarda(left, right):
    while left <= right:
        if left == right:
            print(f"!{right}", flush=True)
            return
        guess = (left + right) // 2
        print(f"?{guess}", flush=True)
        resp = input()
        if resp == "=":
            print(f"!{right}", flush=True)
            return
        elif resp == "<":
            left = guess + 1
        else:
            right = guess - 1

def kinterrogatori(left, right, count, k, bugiardi):
    while left <= right:
        if left == right:
            print(f"!{right}", flush=True)
            return
        guess = (left + right) // 2
        print(f"?{guess}", flush=True)
        resp = input()
        if resp == "=":
            print(f"!{right}", flush=True)
            return
        if bugiardi[count % k]:
            if resp == "<":
                left = guess + 1
            else:
                right = guess - 1
        else:
            if resp == "<":
                right = guess - 1
            else:
                left = guess + 1
        count += 1


test = int(input())
for _ in range(test):
    n, k, b = map(int, input().strip().split())
    if k == 1:
        if b == 0:
            ricercabinaria(1, n)
        else:
            print("?1", flush=True)
            resp = input()
            if resp == "<":
                ricercabinaria_bugiarda(1, n)
            else:
                ricercabinaria(1, n)
    else:
        bugiardi = [0] * k
        for i in range(k):
            print("?1", flush=True)
            resp = input()
            if resp == "<":
                bugiardi[i] = 1
            elif resp == "=":
                print("!1", flush=True)
                break
        kinterrogatori(1, n, 0, k, bugiardi)