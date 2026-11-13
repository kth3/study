def solution(s, skip, index):

    alpha = [chr(i) for i in range(ord('a'), ord('z') + 1) if chr(i) not in skip]
    
    answer = ''

    for char in s:
        cur_idx = alpha.index(char)
        new_idx = (cur_idx + index) % len(alpha)
        answer += alpha[new_idx]
        
    return answer