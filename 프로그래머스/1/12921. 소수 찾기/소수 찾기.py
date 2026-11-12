def solution(n):
    answer = 0
    for x in range(2, n+1):
        for y in range(2, int(x**0.5)+1):
            if not x % y:
                break
        else:
            answer += 1
    return answer