def solution(rank, attendance):
    students = sorted([
        (r, i) for i, (r, att) in enumerate(zip(rank, attendance)) if att
    ])

    a = students[0][1]
    b = students[1][1]
    c = students[2][1]

    return 10000 * a + 100 * b + c