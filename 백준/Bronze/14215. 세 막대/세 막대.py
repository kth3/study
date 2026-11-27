sides = sorted(map(int, input().split()))
x, y, z = sides

if x + y > z:
    print(x + y + z)
else:
    print(2 * (x + y) - 1)