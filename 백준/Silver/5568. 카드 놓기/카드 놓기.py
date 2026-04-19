n = int(input())
k = int(input())
arr = [input() for _ in range(n)]
visited = [False] * n
rst = set()
def solve(depth, cur):
    if depth == k:
        rst.add(cur)
        return
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            solve(depth + 1, cur + arr[i])
            visited[i] = False
solve(0,'')
print(len(rst))
