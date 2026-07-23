def solution(emergency):
    answer = []
    tmp = sorted(emergency, reverse=True)
    tmp_dict = {}
    for t in tmp:
        tmp_dict[t] = tmp.index(t) + 1
    for e in emergency:
        answer.append(tmp_dict[e])
    return answer