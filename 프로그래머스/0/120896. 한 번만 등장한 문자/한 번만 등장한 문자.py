def solution(s):
    cnt = {}
    for i in s:
        if i in cnt:
            cnt[i] += 1
        else:
            cnt[i] = 1
    answer = ''.join(sorted([x for x in cnt if cnt[x] == 1]))
    return answer