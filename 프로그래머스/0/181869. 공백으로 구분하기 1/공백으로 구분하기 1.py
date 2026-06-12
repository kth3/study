def solution(my_string):
    answer = []
    tmp = ''
    for s in my_string:
        if s == ' ':
            answer.append(tmp)
            tmp = ''
            continue
        tmp += s
    answer.append(tmp)
    return answer