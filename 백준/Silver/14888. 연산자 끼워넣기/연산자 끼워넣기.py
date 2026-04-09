n = int(input())
nums = list(map(int, input().split()))

a, b, c, d = map(int, input().split())

max_val = -10 ** 9
min_val = 10 ** 9

def solve(idx, cur, a, b, c, d):
    global max_val, min_val

    if idx == n:
        max_val = max(max_val, cur)
        min_val = min(min_val, cur)
        return

    if a > 0:
        solve(idx + 1, cur + nums[idx], a - 1, b, c, d)
    if b > 0:
        solve(idx + 1, cur - nums[idx], a, b - 1, c, d)
    if c > 0:
        solve(idx + 1, cur * nums[idx], a, b, c - 1, d)
    if d > 0:
        solve(idx + 1, int(cur / nums[idx]), a, b, c, d - 1)

solve(1, nums[0], a, b, c, d)

print(max_val)
print(min_val)