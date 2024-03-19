""" THE FRACTIONAL KNAPSACK PROBLEM"""


def fractional_knapsack(capacity: int, weights: list, values: list) -> tuple:
    """Compute the max value of items a knapsack can carry"""
    n = len(values)
    value_per_weight = [(values[i] / weights[i], weights[i], i) for i in range(n)]
    value_per_weight.sort(reverse=True)

    max_value = 0
    selected_item = []

    for vpw, weight, i in value_per_weight:
        if capacity >= weight:
            max_value += values[i]
            selected_item.append(i)
            capacity -= weight
        else:
            max_value += vpw * capacity
            selected_item.append(i)
            break
    return max_value, selected_item


KL = 10
items_weight = [3, 6, 8]
items_value = [50, 60, 100]

print(fractional_knapsack(KL, items_weight, items_value))
