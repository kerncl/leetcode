import re
from collections import Counter

def parser_date(dates, usage):
    date_regex = re.compile("2020-(?P<month>\d{2})-(?P<day>\d{2})")
    months = []
    for date, spend in zip(dates, usage):
        m = date_regex.match(date)
        if m and spend < 0:
            months.append(m.group('month'))
    return Counter(months)

def parser_usage(dates, usage):
    months = {}
    date_regex = re.compile("2020-(?P<month>\d{2})-(?P<day>\d{2})")
    for date, spend in zip(dates, usage):
        m = date_regex.match(date)
        if m and spend < 0:
            if months.get(m.group('month')):
                months[m.group('month')] += spend
            else:
                months[m.group('month')] = spend
    return months

def parser_usage(dates, usage):
    date_regex = re.compile("2020-(?P<month>\d{2})-(?P<day>\d{2})")
    months_spend = {}
    months = []
    for date, spend in zip(dates, usage):
        m = date_regex.match(date)
        if m and spend < 0:
            months.append(m.group('month'))
            if months_spend.get(m.group('month')):
                months_spend[m.group('month')] += spend
            else:
                months_spend[m.group('month')] = spend

    month_count = Counter(months)
    for m, s in months_spend.items():
        if s > -100 and month_count[m] < 3:
            months.remove(m)
    return months


def solution(a, d):
    months_usage = parser_usage(d, a)
    months = parser_date(d, a)
    total = sum(a)
    deduct = 5 * 12 # assume all month didnt consume
    print(months_usage)
    print(months)
    for (month, spend), (month1, count) in zip(months_usage.items(), months.items()):
        print(month, spend, month1, count)
        if spend <= -100 and count >= 3:
            deduct -= 5

    return total - deduct

def parser_usage2(dates, usage):
    date_regex = re.compile("2020-(?P<month>\d{2})-(?P<day>\d{2})")
    months_spend = {}
    months = []
    for date, spend in zip(dates, usage):
        m = date_regex.match(date)
        if m and spend < 0:
            months.append(m.group('month'))
            if months_spend.get(m.group('month')):
                months_spend[m.group('month')] += spend
            else:
                months_spend[m.group('month')] = spend

    month_count = Counter(months)
    for m, s in months_spend.copy().items():
        if s > -100 and month_count.get(m) < 3:
            month_count.pop(m)
    return month_count

def solution2(A,D):
    months = parser_usage2(D, A)
    total = sum(a)
    deduct = 5 * 12 # assume all month didnt consume


    return total - deduct + 5 * len(months)



if __name__ == '__main__':
    tests = [([100, 100, 100, -10], ['2020-12-31', '2020-12-22', '2020-12-03', '2020-12-29'], 230),
             ([180, -50, -25, -25], ['2020-01-01', '2020-01-01', '2020-01-01', '2020-01-31'], 25),
             ([1, -1, 0, -105, 1], ['2020-12-31', '2020-04-04', '2020-04-04', '2020-04-14', '2020-07-12'], -164),
             ([100, 100, -10, -20, -30], ['2020-01-01', '2020-02-01', '2020-02-11', '2020-02-05', '2020-02-08'], 80),
             ([-60, 60, -40, -20], ['2020-10-01', '2020-02-02', '2020-10-10', '2020-10-30'], -115)]
    for i ,(a, d, ans) in enumerate(tests,1):
        print(f"Test {i}")
        myans = solution2(a, d)
        assert myans == ans, f"{i}: Failed for {a} and {d} expected: {ans} got: {myans}"

