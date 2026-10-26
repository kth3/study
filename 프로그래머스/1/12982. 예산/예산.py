def solution(d, budget):
    d.sort()
    
    count = 0
    for cost in d:
        if budget < cost:
            break
        budget -= cost
        count += 1
        
    return count