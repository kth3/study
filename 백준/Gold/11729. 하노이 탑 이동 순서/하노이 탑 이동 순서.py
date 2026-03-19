n = int(input())
def solve(n, start, end, cur):
    if n == 1:
        print(start, end)
        return
    solve(n-1, start, cur, end)
    print(start, end)
    solve(n-1, cur, end, start)
print(2**n - 1)
solve(n, 1, 3, 2)