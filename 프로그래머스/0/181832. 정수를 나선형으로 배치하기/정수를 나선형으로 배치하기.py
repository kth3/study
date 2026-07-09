def solution(n):
    arr = [[0] * n for _ in range(n)]
    cnt = 1
    k = 0

    while cnt <= n**2:

            for i in range(k, n - k):
                arr[k][i] = cnt
                cnt += 1

            for i in range(k + 1, n - k):
                arr[i][n - 1 - k] = cnt
                cnt += 1

            for i in range(n - 2 - k, k - 1, - 1):
                arr[n - 1 - k][i] = cnt
                cnt += 1

            for i in range(n - 2 - k, k, -1):
                arr[i][k] = cnt
                cnt += 1

            k += 1
    return arr