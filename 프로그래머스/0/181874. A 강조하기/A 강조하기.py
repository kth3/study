def solution(myString):
    answer = ''
    for s in myString:
        if s == 'a':
            answer += s.upper()
        else:
            if s != 'A':
                answer += s.lower()
            else:
                answer += s
    return answer