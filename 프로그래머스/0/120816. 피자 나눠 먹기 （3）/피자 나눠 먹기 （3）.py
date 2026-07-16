def solution(slice, n):
    pizza = 1
    while pizza * slice // n == 0:
        pizza += 1
    return pizza