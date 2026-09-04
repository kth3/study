def solution(polynomial):
    x = 0
    c = 0

    for t in polynomial.split(' + '):
        if 'x' in t:
            num = t.replace('x', '')
            x += int(num) if num else 1
        else:
            c += int(t)

    result = []
    if x > 0:
        result.append('x' if x == 1 else f'{x}x')
    if c > 0:
        result.append(str(c))

    return ' + '.join(result)