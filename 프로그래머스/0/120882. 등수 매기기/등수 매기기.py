def solution(score):
    totals = [eng + math for eng, math in score]
    sorted_totals = sorted(totals, reverse=True)
    return [sorted_totals.index(t) + 1 for t in totals]