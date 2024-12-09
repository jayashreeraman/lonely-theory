
prices = [10,4,7,3,9,2,25]

def maxProfit(prices: list[int]):
    min_price = float('inf')
    max_profit = 0

    for i in range(0, len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]
        elif (prices[i] - min_price) > max_profit:
            max_val = prices[i]
            max_profit = prices[i] - min_price
    print(max_profit)
    print(min_price)
    print(max_val)

maxProfit(prices)



