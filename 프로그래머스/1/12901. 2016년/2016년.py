import datetime

def solution(a, b):
    days = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]

    day_idx = datetime.datetime(2016, a, b).weekday()
    
    return datetime.datetime(2016, a, b).strftime("%a").upper()