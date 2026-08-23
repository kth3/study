def solution(a):
    a = a.split()
    n = int(a[0])
    
    for i in range(1, len(a), 2):
        if a[i] == '+':
            n += int(a[i+1])
        else:
            n -= int(a[i+1])
    return n