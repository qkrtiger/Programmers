def solution(date1, date2):
    year1, month1, day1 = date1
    year2, month2, day2 = date2

    if year1 < year2 or (year1 == year2 and (month1 < month2 or (month1 == month2 and day1 < day2))):
        return 1
    else:
        return 0