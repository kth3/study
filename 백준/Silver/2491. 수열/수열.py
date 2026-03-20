import sys
input = lambda: sys.stdin.readline()
n = int(input())
arr = list(map(int, input().split()))
cnt = 1
tmp = 1
tmp2 = 1
for i in range(1, n):
    if arr[i] >= arr[i-1]:
        tmp += 1
    else:
        tmp = 1
    if arr[i] <= arr[i-1]:
        tmp2 += 1
    else:
        tmp2 = 1
    cnt = max(cnt, tmp, tmp2)
print(cnt)