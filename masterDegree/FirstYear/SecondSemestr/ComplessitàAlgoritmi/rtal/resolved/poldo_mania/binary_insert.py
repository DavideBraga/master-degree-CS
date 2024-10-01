def binary_insertion_sort(arr):
    bins = []
    res = [0 for _ in range(len(arr))]
    for x in range(len(arr) - 1, -1, -1):
        if not bins or arr[x] < bins[-1]:
            print(arr[x])
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

def binary_insertion_sort_2(arr):
    bins = []
    res = [0 for _ in range(len(arr))]
    for x in range(len(arr)):
        if not bins or arr[x] > bins[-1]:
            print(arr[x])
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
            res[x] = hi+1
    return res

arr = [3, 0, 4, 2, 5, 1]
print(binary_insertion_sort(arr))
print(binary_insertion_sort_2(arr))
