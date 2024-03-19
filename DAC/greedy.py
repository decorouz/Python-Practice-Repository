# The problem of giving change using the fewest coins.
# Imagine you have a list of coin amounts [1, 5, 10, 25]
# and an amount of change that you want to produce.


def memo_mc(coin_value_list, change, known_results):
    min_coins = change
    if change in coin_value_list:
        known_results[change] = 1
        return 1
    elif change in known_results:
        return known_results[change]
    else:
        for i in [c for c in coin_value_list if c <= change]:
            num_coins = 1 + memo_mc(coin_value_list, change - i, known_results)
            if num_coins < min_coins:
                min_coins = num_coins
                known_results[change] = min_coins
    return min_coins


def dp_make_change(coin_value_list, change):
    # Create a list to store the answers to the sub-problems
    min_coins = [None for _ in range(change + 1)]

    # for each value from 0 to change, compute the min number of coins needed
    for cents in range(change + 1):
        # assume at first that all 1's are used
        min_coins[cents] = cents
        # check if any coin leads to a better solution to our current best.
        for c in coin_value_list:
            if cents >= c:
                min_coins[cents] = min(min_coins[cents], min_coins[cents - c] + 1)
    return min_coins[change]


print(dp_make_change([1, 5, 10, 21, 25], 63))
# print(dp_make_change([1,5,10,21,25], 64))
# print(dp_make_change([2, 3, 5, 10, 20, 30, 50], 78))


# print(memo_mc([1,5,21,25], 63, {}))
