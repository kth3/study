def solution(a, b):
    cnt = 0
    for i in [a, b]:
        if i % 2 != 0:
            cnt += 1
    if cnt == 2:
        return a**2 + b**2
    elif cnt == 1:
        return 2 * (a+b)
    else:
        return abs(a-b)