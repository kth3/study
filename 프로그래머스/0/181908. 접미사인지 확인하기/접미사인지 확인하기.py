def solution(my_string, is_suffix):
    answer = 0
    check = []
    for idx in range(len(my_string)):
        check.append(my_string[-idx:])
    if is_suffix in check:
        answer = 1
    return answer