def solution(n):
    answer = [x for x in range(1, n+1) if not n % x]
    return answer