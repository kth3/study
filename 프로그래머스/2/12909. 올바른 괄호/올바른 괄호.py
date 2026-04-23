def solution(s):
    solve = True
    stack = []
    for r in s:
        if r == '(':
            stack.append(r)
        else:
            if stack:
                stack.pop()
            else:
                solve = False
                break
    else:
        if stack:
            solve = False
    return solve
    