def solution(n):
    answer = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            if d not in answer:
                answer.append(d)
            n //= d
        else:
            d += 1
    if n > 1 and n not in answer:
        answer.append(n)
    return answer