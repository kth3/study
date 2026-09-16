def solution(babbling):
    words = ["aya", "ye", "woo", "ma"]
    answer = 0

    for word in babbling:
        for valid in words:
            word = word.replace(valid, " ")
        if not word.strip():
            answer += 1

    return answer