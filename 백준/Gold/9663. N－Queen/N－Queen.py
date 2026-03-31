n = int(input())
ans = 0
col = [False] * n
diag1 = [False] * (2 * n) # / 방향 대각선
diag2 = [False] * (2 * n) # \ 방향 대각선

def solve(row):
    global ans
    if row == n:
        ans += 1
        return

    for i in range(n):
        # 열과 두 대각선이 모두 비어있어야 함
        if not col[i] and not diag1[row + i] and not diag2[row - i + n]:
            col[i] = diag1[row + i] = diag2[row - i + n] = True
            # 행은 1차원으로 압축하여 인덱스로 관리함으로써, 중복을 방지함.
            solve(row + 1)
            # 백트래킹: 다시 False로 원상복구
            col[i] = diag1[row + i] = diag2[row - i + n] = False

solve(0)
print(ans)