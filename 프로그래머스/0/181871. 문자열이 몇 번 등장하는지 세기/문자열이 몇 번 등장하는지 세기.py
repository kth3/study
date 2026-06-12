def solution(myString, pat):
    answer = 0
    for s in range(0, len(myString)):
        if myString[s:s+len(pat)] == pat:
            answer += 1
    return answer