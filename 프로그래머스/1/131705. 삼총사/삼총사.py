def solution(number):
    answer = 0
    n = len(number)

    def dfs(start, depth, current_sum):
        nonlocal answer

        if depth == 3:
            if current_sum == 0:
                answer += 1
            return
        
        for i in range(start, n):
            dfs(i + 1, depth + 1, current_sum + number[i])

    dfs(0, 0, 0)
    
    return answer