def solution(numbers):
    answer = []
    for i in range(len(numbers)-1):
        for j in range(i+1, len(numbers)):
            if (num:=numbers[i] + numbers[j]) not in answer:
                answer.append(num)
    return sorted(answer)