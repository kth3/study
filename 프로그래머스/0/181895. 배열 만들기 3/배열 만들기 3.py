def solution(arr, intervals):
    answer = []
    for i in intervals:
        a, b = i
        answer += arr[a:b+1]
    return answer