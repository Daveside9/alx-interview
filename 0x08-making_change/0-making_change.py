def makeChange(coins, total):
    if total <= 0:
        return 0

    # Create a list to store the fewest number of coins needed for each value from 0 to total
    min_coins = [float('inf')] * (total + 1)

    # Base case: 0 coins needed to make a total of 0
    min_coins[0] = 0

    # Iterate through all possible values from 1 to total
    for value in range(1, total + 1):
        # Check each coin denomination
        for coin in coins:
            # If the coin value is less than or equal to the current value
            if coin <= value:
                # Update the minimum number of coins needed for the current value
                min_coins[value] = min(min_coins[value], 1 + min_coins[value - coin])

    # If the minimum number of coins for the total is still infinity, it means it's not possible to make the total
    if min_coins[total] == float('inf'):
        return -1

    return min_coins[total]

