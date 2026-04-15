k = int(input())
arr = input().split()

visited = [False] * 10
results = []

def check(a, b, op):
    if op == '<':
        return a < b
    if op == '>':
        return a > b
    return False

def solve(depth, s):
    if depth == k + 1:
        results.append(s)
        return

    for i in range(10):
        if not visited[i]:
            if depth == 0 or check(s[-1], str(i), arr[depth-1]):
                visited[i] = True
                solve(depth + 1, s + str(i))
                visited[i] = False

solve(0, "")

print(results[-1])
print(results[0])