def solution(price, money, count):
    result = 0
    for c in range(count):
        result += price * (c+1)
    return 0 if money >= result else result - money