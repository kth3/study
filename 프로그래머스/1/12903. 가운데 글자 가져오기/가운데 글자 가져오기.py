def solution(s):
    k = len(s); l = k // 2
    return s[l] if k % 2 else s[l-1:l+1]