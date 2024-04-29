import math
def findMax(piles):
    maxi = float('-inf')
    n = len(piles)

    for i in range(n):
        maxi = max(maxi, piles[i])
    return maxi

def JackiesBananas(piles, h):
    if not piles:
        return 0

    left, right = 1, max(piles)

    while left <= right:
        middle = (left + right) // 2
        total_hour = calculateTotalHours(piles, middle)
        if total_hour <= h:
            right = middle - 1
        else:
            left = middle + 1
    return left

def calculateTotalHours(piles, k):
    total_hour = 0
    n = len(piles)

    for i in range(n):
        total_hour += math.ceil(piles[i] / k)
    return total_hour

