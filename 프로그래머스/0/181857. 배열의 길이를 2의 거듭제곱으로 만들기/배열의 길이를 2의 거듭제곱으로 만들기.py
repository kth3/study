def solution(arr):
    n = len(arr)
    target = 1
    while target < n:
        target *= 2
    return arr + [0] * (target - n)