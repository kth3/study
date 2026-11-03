def solution(s):
    answer = ''
    num = '0123456789'
    text = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }
    cur = ''
    for x in s:
        if x in num:
            answer += x 
        else:
            cur += x
            if cur in text:
                answer += text[cur]
                cur = ''
                
    return int(answer)
            