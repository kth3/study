def solution(ineq, eq, n, m):
    answer = ''
    if ineq == '<':
        if eq == '=':
            answer = bool(n <= m)
        else:
            answer = bool(n < m)
    else:
        if eq == '=':
            answer = bool(n >= m)
        else:
            answer = bool(n > m)
    
    return int(answer)