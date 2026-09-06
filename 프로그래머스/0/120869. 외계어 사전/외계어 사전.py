def solution(spell, dic):
    target = set(spell)
    for word in dic:
        if set(word) == target:
            return 1
    return 2