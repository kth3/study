s = [int(input()) for _ in range(3)]
length = len(set(s))
ans = ''
if sum(s) != 180:
  ans = 'Error'
else:
  if length > 2:
    ans = 'Scalene'
  elif length == 2:
    ans = 'Isosceles'
  elif length < 2:
    ans = 'Equilateral'
print(ans)