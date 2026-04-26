def solution(a, b):
    rst1 = int(str(a) + str(b))
    rst2 = 2 * int(a) * int(b)
    answer = max(rst1, rst2)
    return answer