n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]
visited = [False] * n
min_diff = float('inf')

def solve(depth, idx):
    global min_diff
    
    if depth == n // 2:
        start_score = 0
        link_score = 0
        
        for i in range(n):
            for j in range(i + 1, n):
                if visited[i] and visited[j]:
                    start_score += s[i][j] + s[j][i]
                elif not visited[i] and not visited[j]:
                    link_score += s[i][j] + s[j][i]
        
        min_diff = min(min_diff, abs(start_score - link_score))
        return
    
    for i in range(idx, n):
        if not visited[i]:
            visited[i] = True
            solve(depth + 1, i + 1)
            visited[i] = False

solve(0, 0)
print(min_diff)