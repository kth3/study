def solution(n, words):
    answer = [0, 0]
    arr = [words[0]]
    for idx in range(1, len(words)):
        if words[idx] in arr or (words[idx][0] != words[idx-1][-1]):
            answer = [idx%n+1, idx//n+1]
            break
        else:
            arr.append(words[idx])
    

    return answer