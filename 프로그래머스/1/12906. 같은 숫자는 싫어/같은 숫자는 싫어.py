def solution(arr):
    answer = []
    last = -1
    for a in arr:
        if a != last:
            answer.append(a)
            last = a
    return answer