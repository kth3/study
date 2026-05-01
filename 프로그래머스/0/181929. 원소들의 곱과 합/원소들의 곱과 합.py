def solution(num_list):
    answer = True
    sum_num = sum(num_list) ** 2
    tmp = 1
    for num in num_list:
        if tmp > sum_num:
            answer = False
            break
        tmp *= num
    else:
        if tmp > sum_num:
            answer = False
                
    return int(answer)