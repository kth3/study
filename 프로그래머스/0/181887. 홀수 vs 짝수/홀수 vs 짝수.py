def solution(num_list):
    even = 0
    odd = 0
    for idx, num in enumerate(num_list):
        if idx % 2 == 0:
            even += num
        else:
            odd += num
    return max(even, odd)