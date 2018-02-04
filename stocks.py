def get_max_profit(stock_prices_yesterday):

    min_price = stock_prices_yesterday[0]
    max_profit = 0

    if len(stock_prices_yesterday) < 2:
        print "Haha! got you"

    for current_price in stock_prices_yesterday:
        #Keep minimum price
        min_price = min(min_price, current_price)
        #Keep a score of potential profit
        potential_profit = current_price - min_price
        #Update maximum profit
        max_profit = max(max_profit, potential_profit)

    return max_profit


print(get_max_profit([7, 4, 8, 4, 9]))










