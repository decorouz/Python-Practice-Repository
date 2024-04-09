"""Imagine that you are a thief breaking into a house. There are so many valuables to steal, 
but you’re just one person who can only carry so much. Each item has a weight and value, 
and your goal is to maximize the total value of items while remaining within the weight limit of your knapsack. 
Create a knapsack() function that takes in:

    - the total amount of weight you can carry
    - an array of the weights of all of the items
    - an array of the values of all of the items
    - and returns the maximum value that you will be able to carry.

For example, let’s say your knapsack can carry 10 units of weight. 
The item weights are [3, 6, 8] and their values are [50, 60, 100]. 
Your knapsack function should return 110 since you can carry the first and second items, 
whose values total 110. 
If you tried to carry the third item, which has the value of 100, you wouldn’t 
be able to fit anything else in the knapsack.


Write a test case for this challenge"""


def knapsack(capacity: int, weights: list[int], values: list[int]) -> tuple:
    """Find the maximum value items a knapsack can carry.

    Args:
        capacity (int): maximum capacity of the knapsack
        weights (list[int]): weights of the items
        values (list[int]): value of the items

    Returns:
        tuple: value and index of the items
    """
    n = len(values)
    # Initialize all possible combination of items
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    for i in range(1, (n + 1)):
        for w in range(1, capacity + 1):
            if weights[i - 1] > w:
                dp[i][w] = dp[i - 1][w]
            else:
                dp[i][w] = max(
                    dp[i - 1][w], values[i - 1] + dp[i - 1][w - weights[i - 1]]
                )
    print(dp)
    # Get the selected items
    selected_items = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(i - 1)
            w -= weights[i - 1]

    selected_items.reverse()
    return (dp[n][capacity],)


# Driver code
if __name__ == "__main__":
    KL = 10
    items_weight = [1, 6, 2, 2, 8]
    items_value = [50, 60, 300, 2, 100]
    result = knapsack(KL, items_weight, items_value)
    print(result)
