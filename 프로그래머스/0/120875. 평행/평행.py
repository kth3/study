def get_slope(p1, p2):
    return (p2[1] - p1[1]) / (p2[0] - p1[0])


def solution(dots):
    pairs = [
        ((0, 1), (2, 3)),
        ((0, 2), (1, 3)),
        ((0, 3), (1, 2)),
    ]

    for (a, b), (c, d) in pairs:
        if get_slope(dots[a], dots[b]) == get_slope(dots[c], dots[d]):
            return 1

    return 0