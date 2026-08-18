def solution(my_string, num1, num2):
    n = list(my_string)
    n[num1], n[num2] = n[num2], n[num1]
    return ''.join(n)