def solution(n):
    tmp = set()
    for i in range(1, n+1):
        if n % i == 0:
            tmp.add((i, n//i))
    return len(tmp)