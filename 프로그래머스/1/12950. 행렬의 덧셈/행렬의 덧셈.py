def solution(arr1, arr2):
    return [[c1 + c2 for c1, c2 in zip(row1, row2)] for row1, row2 in zip(arr1, arr2)]