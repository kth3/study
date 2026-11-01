def solution(s, n):
    result = []
    for char in s:
        if char == ' ':
            result.append(' ')
        elif 'a' <= char <= 'z':
            shifted = ord('a') + (ord(char) - ord('a') + n) % 26
            result.append(chr(shifted))
        elif 'A' <= char <= 'Z':
            shifted = ord('A') + (ord(char) - ord('A') + n) % 26
            result.append(chr(shifted))
            
    return ''.join(result)