def solution(participant, completion):
    d = {}
    for p in participant:
        if p in d:
            d[p] += 1
        else:
            d[p] = 1
    for c in completion:
        d[c] -= 1
    
    for n in d:
        if d[n] > 0:
            return n
    