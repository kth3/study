def solution(s):
    l = list(s.split())
    for i, v in enumerate(l):
        if v == 'Z':
            l.pop(i-1)
    print(l)
    return sum([int(x) for x in l if x != 'Z'])