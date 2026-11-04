def solution(array, commands):
    answer = []
    for c in commands:
        i, j, k = c
        t = array[i-1:j]
        t.sort()
        answer.append(t[k-1])
    return answer