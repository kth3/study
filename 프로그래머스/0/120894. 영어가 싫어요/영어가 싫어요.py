def solution(numbers):
    num = {"zero" : '0', "one" : '1', "two" : '2', "three" : '3', "four" : '4', "five" : '5', "six" : '6', "seven" : '7', "eight" : '8', "nine" : '9'}
    answer = ''
    tmp = ''
    for n in numbers:
        tmp += n
        if tmp in num:
            answer += num[tmp]
            tmp = ''
    return int(answer)