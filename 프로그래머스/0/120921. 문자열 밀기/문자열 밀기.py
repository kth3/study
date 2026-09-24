from collections import deque

def solution(A, B):
    q = deque(A)
    for i in range(len(A)):
        if ''.join(q) == B:
            return i
        q.rotate(1)
    return -1