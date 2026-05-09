def solution(arr, queries):
    answer = []
    for query in queries:
        s, e, k = query
        tmp_list = []
        for i in arr[s:e+1]:
            if i > k:
                tmp_list.append(i)
        if tmp_list:
            answer.append(min(tmp_list))
        else:
            answer.append(-1)
                
    return answer