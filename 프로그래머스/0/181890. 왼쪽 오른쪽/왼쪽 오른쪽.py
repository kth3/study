def solution(str_list):
    answer = []
    for idx, s in enumerate(str_list):
        if s == 'l':
            answer += str_list[:idx]
            return answer
        elif s == 'r':
            answer += str_list[idx+1:]
            return answer
    return answer