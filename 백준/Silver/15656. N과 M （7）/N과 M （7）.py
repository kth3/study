n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
tmp = []
def solve():
    if len(tmp) == m:
        print(' '.join(map(str, tmp)))
        return
    for i in range(n):
        tmp.append(arr[i])
        solve()
        tmp.pop()
solve()