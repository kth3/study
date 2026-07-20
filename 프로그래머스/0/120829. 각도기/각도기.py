def solution(angle):
    answer = 1
    if angle == 180:
        answer += 3
    elif angle > 90:
        answer += 2
    elif angle == 90:
        answer += 1
    return answer