def calc_max_starting(arr):
    bins = []
    res = [0 for _ in range(len(arr))]
    for x in range(len(arr) - 1, -1, -1):
        if not bins or arr[x] < bins[-1]:
            bins.append(arr[x])
            res[x] = len(bins)
        else:
            lo, hi = 0, len(bins) - 1
            while lo < hi:
                mid = (lo + hi) // 2
                if bins[mid] > arr[x]:
                    lo = mid + 1
                else:
                    hi = mid
            bins[hi] = arr[x]
            res[x] = hi+1

    return res

def calc_max_ending(arr):
    bins = []
    res = [0 for _ in range(len(arr))]
    for x in range(len(arr)):
        if not bins or arr[x] > bins[-1]:
            bins.append(arr[x])
            res[x] = len(bins)
        else:
            lo, hi = 0, len(bins) - 1
            while lo < hi:
                mid = (lo + hi) // 2
                if bins[mid] < arr[x]:
                    lo = mid + 1
                else:
                    hi = mid
            bins[hi] = arr[x]
            res[x] = hi + 1
    return res


n = int(input())

for _ in range(n):
    lenght = int(input())
    array = list(map(int, input().strip().split()))
    sol = calc_max_starting(array)
    res = calc_max_ending(array)
    print(" ".join(str(sol[x] + res[x] - 1) for x in range(len(sol))))
