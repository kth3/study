def solution(arr, k):
    answer = []
    for a in arr:
        if len(answer) == k:
            break
        if not a in answer:
            answer.append(a)
    if len(answer) < k:
        answer.extend([-1] * (k - len(answer)))
    return answer