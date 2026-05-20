def solution(a, b, c, d):
    answer = 1
    dice = [a, b, c, d]
    dice_set = list(set(dice))
    dice_cnt = {}
    
    for d in dice:
        if d in dice_cnt:
            dice_cnt[d] += 1
        else:
            dice_cnt[d] = 1
    length = len(dice_cnt)
    if length == 4:
        answer = min(dice_cnt.keys())
    elif length == 3:
        for num ,value in dice_cnt.items():
            if value == 1:
                answer *= num
    elif length == 2:
        p = 0
        q = 0
        for num, value in dice_cnt.items():
            if value == 2:
                answer = (dice_set[0] + dice_set[1]) * abs(dice_set[0] - dice_set[1])
                break
            else:
                if value == 3:
                    p = num
                elif value == 1:
                    q = num
                answer = (10 * p + q) ** 2
    elif length == 1:
        answer = 1111 * dice_set[0]
    
    return answer