def solution(arr):
    r = len(arr)
    c = len(arr[0])
    if r > c:
        for a in arr:
            a += [0] * (r-c)
    else:
        for _ in range(c-r):
            arr.append([0] * c)
    return arr