def solution(quiz):
    answer = []
    for q in quiz:
        x, a, y, b, z = q.split()
        if a == "+": 
            s = int(x) + int(y)
        else:
            s = int(x) - int(y)
        answer.append("O" if s == int(z) else "X")
    return answer