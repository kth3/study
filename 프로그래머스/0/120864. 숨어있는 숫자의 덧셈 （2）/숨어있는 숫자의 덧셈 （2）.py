def solution(my_string):
    num = "".join(c if c.isdigit() else " " for c in my_string).split()
    return sum(int(x) for x in num)