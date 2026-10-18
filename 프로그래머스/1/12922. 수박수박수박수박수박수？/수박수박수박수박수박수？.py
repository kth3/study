def solution(n):
    arr = ['수', '박']
    return ''.join([arr[i%2] for i in range(n)])