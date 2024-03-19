"""Basic test for knapsack function"""

from knapsack import knapsack


def test_knapsack():
    # Test case
    capacity = 10
    weights = [3, 6, 2, 2, 8]
    values = [50, 60, 300, 2, 100]
    expected_max_value = 400
    expected_selected_items = [2, 4]

    # call the function to get the results
    actual_max_value, actual_selected_items = knapsack(capacity, weights, values)

    # Assert actual results matches with expected results
    assert actual_max_value == expected_max_value
    assert actual_selected_items == expected_selected_items
