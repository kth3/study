def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def solution(n, m):
    gcd_val = gcd(n, m)
    lcm_val = (n * m) // gcd_val
    return [gcd_val, lcm_val]