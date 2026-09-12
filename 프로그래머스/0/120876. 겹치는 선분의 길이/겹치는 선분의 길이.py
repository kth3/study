def solution(lines):
    count = [0] * 200
    
    for start, end in lines:
        for i in range(start, end):
            count[i + 100] += 1
            
    return sum(1 for c in count if c >= 2)