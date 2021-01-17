# Best Time to Buy and Sell Stock

# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# Example 1:
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

# Example 2:
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.


def besttime(nums):
    # Solution 1
    # minimum = min(nums)
    # maximum = minimum
    # for x in range(nums.index(minimum)+1,len(nums)):
    #     if nums[x] > maximum:
    #         maximum = nums[x]
    # return maximum-minimum

    #Solution 2
    max_profit = 0
    for x in range(len(nums)):
        for y in range(x+1,len(nums)):
            profit = nums[y] - nums[x]
            if  profit > 0 and profit > max_profit:
                max_profit = profit
    return max_profit
                 
if __name__ == '__main__':
    list_of_values = [[7,1,5,3,6,4],[7,6,4,3,1]]
    for li in list_of_values:
        print(f'Input is {li}')
        print(f'Best Profit is {besttime(li)}')
