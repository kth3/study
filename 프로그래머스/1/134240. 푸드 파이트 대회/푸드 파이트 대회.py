def solution(food):
    res = []

    for i in range(1, len(food)):
        count = food[i] // 2
        res.append(str(i) * count)

    left = "".join(res)
    
    answer = left + "0" + left[::-1]
    
    return answer