def solution(num_list):
    e = o = 0
    for num in num_list:
        if num % 2 == 0:
            e += 1
        else:
            o += 1
    return [e, o]