def solution(strArr):
    answer = []
    for idx, s in enumerate(strArr):
        if idx % 2 != 0:
            answer.append(s.upper())
        else:
            answer.append(s.lower())
    return answer