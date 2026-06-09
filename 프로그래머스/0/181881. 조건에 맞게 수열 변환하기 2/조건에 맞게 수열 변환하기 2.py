def solution(arr):
    answer = 0
    while True:
        tmp = []
        for a in arr:
            if a % 2 == 0 and a >= 50:
                tmp.append(a//2)
            elif a % 2 != 0 and a < 50:
                tmp.append(a*2+1)
            else:
                tmp.append(a)
        if arr == tmp:
            break
        else:
            arr = tmp
            answer += 1
            
    return answer