def solution(arr):
    answer = []
    start = []
    end = []
    for idx, num in enumerate(arr):
        if num == 2:
            if not start:
                start.append(idx)
            else:
                if end:
                    end[0] = idx
                else:
                    end.append(idx)
    if start:
        if end:
            answer += arr[start[0]:end[0]+1]
        else:
            answer.append(arr[start[0]])
    else:
        answer = [-1]
            
    return answer