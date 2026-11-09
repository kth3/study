def solution(name, yearning, photo):
    arr = {}
    answer = []
    for x, y in zip(name, yearning):
        arr[x] = y
    for p in photo:
        tmp = 0
        for i in p:
            if i in arr:
                tmp += arr[i]
        answer.append(tmp)

    return answer