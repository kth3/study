def solution(k, score):
    answer = []
    arr = []  
    
    for s in score:
        arr.append(s)
        arr.sort(reverse=True)
        
        if len(arr) > k:
            arr.pop()
            
        answer.append(arr[-1])
        
    return answer