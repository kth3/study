while True:
  n = int(input())
  if n == -1:
    break

  ans = [1]
  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      ans.append(i)
      if i != n // i:
        ans.append(n // i)

  if sum(ans) == n:
    ans.sort()
    print(f"{n} = {' + '.join(map(str, ans))}")
  else:
    print(f"{n} is NOT perfect.")