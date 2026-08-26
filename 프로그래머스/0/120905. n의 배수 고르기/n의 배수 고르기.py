def solution(n, numlist):
    a = []
    for num in numlist:
        if num % n == 0:
            a.append(num)
    return a