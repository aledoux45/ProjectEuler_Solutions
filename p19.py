if __name__ == "__main__":
    months = [31,28,31,30,31,30,31,31,30,31,30,31]
    answer = 0
    n_days = -1 # Jan 1st 1900 is on a Monday
    year = 1900
    while year < 2001:
        for m, month in enumerate(months):
            if year > 1900 and n_days % 7 == 0:
                answer += 1
            # add days
            n_days += month
            if m == 2 and year % 4 == 0 and year % 100 != 0:
                n_days += 1
            elif m == 2 and year % 400 == 0:
                n_days += 1
        year += 1
    print(answer)