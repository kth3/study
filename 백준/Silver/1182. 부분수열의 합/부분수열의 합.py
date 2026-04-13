n, s = map(int, input().split())
nums = list(map(int, input().split()))

count = 0

def solve(idx, current_sum):
    global count

    if idx == n:
        if current_sum == s:
            count += 1
        return

    solve(idx + 1, current_sum + nums[idx])

    solve(idx + 1, current_sum)

solve(0, 0)

if s == 0:
    count -= 1

print(count)