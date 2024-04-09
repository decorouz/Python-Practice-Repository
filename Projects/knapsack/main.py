def main(capacity, weights, values):
    n = len(weights)

    max_val_table = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, (n + 1)):
        for current_capacity in range(1, capacity + 1):
            if weights[i - 1] > current_capacity:
                max_val_table[i][current_capacity] = max_val_table[i - 1][
                    current_capacity
                ]
            else:
                max_val_table[i][current_capacity] = max(
                    max_val_table[i - 1][current_capacity],
                    (
                        values[i - 1]
                        + max_val_table[i - 1][current_capacity - weights[i - 1]]
                    ),
                )

    selected_items = []
    for i in range(n, 0, -1):
        if max_val_table[i][capacity] != max_val_table[i - 1][capacity]:
            selected_items.append(i - 1)
            capacity -= weights[i - 1]

    selected_items.reverse()
    return max_val_table[n][capacity], selected_items


# Driver code
if __name__ == "__main__":
    KL = 10
    items_weight = [3, 6, 2, 2, 8]
    items_value = [50, 60, 300, 2, 100]
    print(main(KL, items_weight, items_value))
