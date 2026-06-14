def solution(myString):
    answer = sorted([x for x in myString.split('x') if x != ''])
    
    return answer