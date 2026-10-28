def solution(s):
    answer = ''
    idx = 0
    
    for a in s:
        if a == ' ':
            answer += ' '
            idx = 0
        else:
            if idx % 2 != 0:
                answer += a.lower()
            else:
                answer += a.upper()
            idx += 1
            
    return answer