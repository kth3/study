def solution(binomial):
    tmp = binomial.split()
    a, op, b = tmp
    a, b = int(a), int(b)
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    else:
        return a * b