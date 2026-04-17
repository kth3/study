n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

min_diff = float('inf')

def solve(idx, a, b, cnt):
    global min_diff

    if idx == n:
        if cnt > 0:
            min_diff = min(min_diff, abs(a - b))
        return

    solve(idx + 1, a * arr[idx][0], b + arr[idx][1], cnt + 1)

    solve(idx + 1, a, b, cnt)

solve(0, 1, 0, 0)
print(min_diff)