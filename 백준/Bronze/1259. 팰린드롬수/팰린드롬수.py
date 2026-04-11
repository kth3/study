import sys
for line in sys.stdin:
    line = line.rstrip()
    if line == '0':
        break
    left = 0
    right = len(line) - 1
    find = True
    while left < right:
        if line[left] != line[right]:
            find = False
            break
        left += 1
        right -= 1
    if find:
        print('yes')
    else:
        print('no')