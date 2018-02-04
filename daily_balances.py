def show_balances(daily_balances):

    num_balances = len(daily_balances)

    for days in range(num_balances - 3, num_balances - 1):
        #print(days)
        balance_slice = daily_balances[days: days + 2]
        days_ago = num_balances - days
        print("slicing %d days ago: %s" % (abs(days_ago), balance_slice))


show_balances([107.92, 108.67, 109.86, 110.15, 452.78, 7845.56, 451.23])
