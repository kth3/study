def solution(my_string):
    answer = ''.join([x for x in my_string if not x in 'aeiuo'])
    return answer