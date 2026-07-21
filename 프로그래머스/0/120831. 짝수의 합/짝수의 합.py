def solution(n):
    answer = 0
    for x in range(2, n+1, 2):
        answer += x
    return answer