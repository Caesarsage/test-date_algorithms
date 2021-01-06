def date_solution(d):
    import datetime, collections
    from collections import defaultdict
    output = {}
    count = defaultdict(int)
    days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]

    for date in d:
        date_details = date.split("-")
        year, month, day = date_details
        #print(date_details)

        week_day = datetime.date(int(year), int(month), int(day)).strftime("%a")
        #print(week_day)
        count[week_day]+= d[date]
        #print(d[date])

#CONDICTION 3 
    commmon_difference = (count["Sun"] - count["Mon"])//6

    for i in range(1,len(days)):
        curr_day = days[i]
        prev_day = days[i-1]
        if count[curr_day] == 0:
            count[curr_day] = count[prev_day] + commmon_difference

##############################################################################
    for day in days:
        output[day] = count[day]

    return output

d1 = {"2020-01-01": 4, "2020-01-02": 4, "2020-01-03": 6, "2020-01-04": 8, "2020-01-05": 2, "2020-01-06": -6, "2020-01-07": 2, "2020-01-08": -2}
d2 = {"2020-01-01": 6, "2020-01-04":12, "2020-01-05":14, "2020-01-06":2, "2020-01-07":4}
print(date_solution(d1))
print(date_solution(d2))

