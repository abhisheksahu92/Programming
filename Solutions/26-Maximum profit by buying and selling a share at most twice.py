# Maximum profit by buying and selling a share at most twice

# In a daily share trading, a buyer buys shares in the morning and sells it on the same day. If the trader is allowed to make at most 2 transactions in a day, whereas the second transaction can only start after the first one is complete (Sell->buy->sell->buy). Given stock prices throughout the day, find out the maximum profit that a share trader could have made.

# Input:   price[] = {10, 22, 5, 75, 65, 80}
# Output:  87
# Trader earns 87 as sum of 12 and 75
# Buy at price 10, sell at 22, buy at 5 and sell at 80

# Input:   price[] = {2, 30, 15, 10, 8, 25, 80}
# Output:  100
# Trader earns 100 as sum of 28 and 72
# Buy at price 2, sell at 30, buy at 8 and sell at 80

# Input:   price[] = {100, 30, 15, 10, 8, 25, 80};
# Output:  72
# Buy at price 8 and sell at 80.

# Input:   price[] = {90, 80, 70, 60, 50}
# Output:  0
# Not possible to earn.

def sellBuy(nums):
    max_profit,times  = 0,0
    bought = False
    buy = None
    for x in range(len(nums)):
        if times < 2:
            if not bought:
                if nums[x] < nums[x+1]:
                    buy = x
                    bought = True
                    times = times + 1
            else:
                if times == 1:
                    if buy < nums[x] and nums[x+1] < nums[x]:
                        max_profit = max_profit + (nums[x] - buy)
                        bought = False
                else:
                    max_profit = max_profit + max()
        else:
            print(f'Maximum Profit: {max_profit}')
            
    print(nums)
        
if __name__ == '__main__':
    list_of_values = [[10, 22, 5, 75, 65, 80]]
    
    for li in list_of_values:
        print(f'Input is {li}')
        sellBuy(li)