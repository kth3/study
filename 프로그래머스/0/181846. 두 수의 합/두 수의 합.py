import sys
sys.set_int_max_str_digits(200000) # 자릿수 제한 해제

def solution(a, b):
    answer = str(int(a)+int(b))
    return answer