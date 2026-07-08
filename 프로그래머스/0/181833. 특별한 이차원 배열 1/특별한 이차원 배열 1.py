def solution(n):
    answer = []
    for i in range(n):
        tmp = [0] * n
        tmp[i] = 1
        answer.append(tmp)
    return answer