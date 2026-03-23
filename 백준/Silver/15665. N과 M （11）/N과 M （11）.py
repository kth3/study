n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
tmp = []

def solve():
    if len(tmp) == m:
        print(' '.join(map(str, tmp)))
        return
    last_n = 0
    for i in range(n):
        if arr[i] != last_n:
            tmp.append(arr[i])
            last_n = arr[i]
            solve()
            tmp.pop()
solve()