# 1. 입력 및 초기화
board = [list(map(int, input().split())) for _ in range(9)]
zeros = [(r, c) for r in range(9) for c in range(9) if board[r][c] == 0]

# 2. 검역소(방문 배열) 만들기: [번호][숫자]
# row_check[3][5] == True 이면, 3행에 이미 5가 있다는 뜻
row_check = [[False] * 10 for _ in range(9)]
col_check = [[False] * 10 for _ in range(9)]
square_check = [[False] * 10 for _ in range(9)]

# 3. 초기 보드 상태를 검역소에 기록
for r in range(9):
    for c in range(9):
        if board[r][c] != 0:
            num = board[r][c]
            row_check[r][num] = True
            col_check[c][num] = True
            # 사각형 번호 공식: (r // 3) * 3 + (c // 3)
            square_check[(r // 3) * 3 + (c // 3)][num] = True


def solve(idx):
    # 모든 빈칸을 다 채웠다면 종료
    if idx == len(zeros):
        for row in board:
            print(*row)
        exit(0)  # 답이 하나만 나오면 즉시 전체 종료

    r, c = zeros[idx]
    sq_idx = (r // 3) * 3 + (c // 3)  # 현재 칸이 속한 사각형 번호

    for num in range(1, 10):
        # 세 가지 검역소를 단 한 번에 통과해야 함!
        if not row_check[r][num] and not col_check[c][num] and not square_check[sq_idx][num]:
            # 숫자 써넣기 및 검역소 폐쇄
            board[r][c] = num
            row_check[r][num] = col_check[c][num] = square_check[sq_idx][num] = True

            solve(idx + 1)

            # 백트래킹: 숫자 지우기 및 검역소 개방
            board[r][c] = 0
            row_check[r][num] = col_check[c][num] = square_check[sq_idx][num] = False

solve(0)