def solution(n):
    answer = 1
    i = 1
    while i * answer < n:
        answer += 1
        i *= answer
    return answer