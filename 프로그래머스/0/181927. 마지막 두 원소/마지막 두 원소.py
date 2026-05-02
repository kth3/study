def solution(num_list):
    answer = num_list
    num1 = num_list[-1]
    num2 = num_list[-2]
    if num1 > num2:
        answer.append(num1 - num2)
    else:
        answer.append(num1 * 2)
    
    return answer