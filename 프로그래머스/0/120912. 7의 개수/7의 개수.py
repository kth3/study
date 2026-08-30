def solution(array):
    a = ''
    for x in array:
        a += str(x)
    return a.count('7')