def solution(myString, pat):
    last_idx = -1
    for i in range(len(myString) - len(pat) + 1):
        if myString[i : i + len(pat)] == pat:
            last_idx = i

    return myString[: last_idx + len(pat)]