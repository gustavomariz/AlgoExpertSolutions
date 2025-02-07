def nonConstructibleChange(coins):
    # Write your code here.
    if coins == []:
        return 1
        
    coins.sort()
    
    sum = 0
    for i in range(len(coins)):
        if coins[i] > sum + 1:
            return sum + 1
        else:
            sum += coins[i]
    return sum + 1
           
