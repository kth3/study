def solution(order):
    answer = 0
    order = str(order)
    for x in order:
        if x in '369':
            answer += 1
    return answer