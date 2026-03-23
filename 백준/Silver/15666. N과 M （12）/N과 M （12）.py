n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
tmp = []

def solve(start):
    if len(tmp) == m:
        print(' '.join(map(str, tmp)))
        return
    last_n = 0
    for i in range(start, n):
        if arr[i] != last_n:
            tmp.append(arr[i])
            last_n = arr[i]
            solve(i)
            tmp.pop()
solve(0)