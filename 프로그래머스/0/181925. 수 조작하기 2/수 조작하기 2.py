def solution(numLog):
    answer = ''
    rst = {1: 'w', -1: 's', 10: 'd', -10: 'a'}
    for idx in range(1, len(numLog)):
        answer += rst[numLog[idx] - numLog[idx-1]]
    return answer