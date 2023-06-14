from __future__ import annotations
from typing import List
from time import time

def makeChange(coins: List[int], total: int) -> int:
    if total <= 0:
        return 0

    min_coins = [float('inf')] * (total + 1)
    min_coins[0] = 0

    for value in range(1, total + 1):
        for coin in coins:
            if coin <= value:
                min_coins[value] = min(min_coins[value], 1 + min_coins[value - coin])

    if min_coins[total] == float('inf'):
        return -1

    return min_coins[total]

if __name__ == '__main__':
    # Test case 1
    coins1 = [1, 2, 25]
    total1 = 37
    print(f"Minimum number of coins needed for total {total1}: {makeChange(coins1, total1)}")

    # Test case 2
    coins2 = [1256, 54, 48, 16, 102]
    total2 = 1453
    print(f"Minimum number of coins needed for total {total2}: {makeChange(coins2, total2)}")

