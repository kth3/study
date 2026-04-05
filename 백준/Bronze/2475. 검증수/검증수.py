nums = list(map(int, input().split()))
solve = 0
for num in nums:
    solve += num ** 2
print(solve % 10)