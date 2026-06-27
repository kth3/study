def solution(arr, n):
    is_odd = len(arr) % 2 != 0
    for i in range(len(arr)):
        if is_odd and i % 2 == 0:
            arr[i] += n
        elif not is_odd and i % 2 != 0:
            arr[i] += n
    return arr