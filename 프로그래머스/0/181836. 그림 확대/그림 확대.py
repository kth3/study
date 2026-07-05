def solution(picture, k):
    answer = []
    for p in picture:
        tmp = ''
        for i in p:
            tmp += i * k
        for _ in range(k):
            answer.append(tmp)
    return answer