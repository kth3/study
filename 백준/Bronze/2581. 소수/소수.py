n = int(input()); m = int(input())
arr = []

for i in range(n, m+1):
    if i < 2:
        continue
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            break
    else:
        arr.append(i)
if arr:
    print(sum(arr))
    print(arr[0])
else:
    print(-1)