def solution(left, right):
    answer = 0
    for x in range(left, right+1):
        cnt = 0
        for y in range(1, int(x**0.5)+1):
            if x % y == 0:
                cnt += 1
                if y != x//y:
                    cnt += 1
        if cnt % 2 == 0:
            answer += x
        else:
            answer -= x
    return answer
    