def solution(a, b):
    month_day = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = sum(month_day[:a-1]) + b + 4
    week = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
    answer = week[day % 7]
    return answer