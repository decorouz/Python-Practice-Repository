# Zip takes iterables as arguements and returns an iterator.
# The iterator generate a list of tuples containing elements from each iterable.

numbers = [1, 2, 3,4,5,6,7]
letters = ['a', 'b', 'c', "d"]
operators = ['*', '/', '+']

zipped = zip(numbers, letters)
list(zipped)


# traversing list in parallel
# Traversing two or more iterables at once

for l, n, o in zip(letters, numbers, operators):
    print(f'Letter: {l}')
    print(f'Number: {n}')
    print(f'Operator: {o}')

# Traversing Dictionaries in Parallel

dict_one = {'name': 'John', 'last_name': 'Doe', 'job': 'Python Consultant'}
dict_two = {'name': 'Jane', 'last_name': 'Doe', 'job': 'Community Manager'}

for (k1,v1), (k2,v2) in zip(dict_one.items(), dict_two.items()):
    print(k1, "->", v1)
    print(k2, "->", v2)


# Calculating in Pairs
# Use zip function to make some quick calculations

total_sales = [52000.00, 51000.00, 48000.00]
prod_cost = [46800.00, 45900.00, 43200.00]
# Calculate the monthly income.


for sales, cost in zip(total_sales, prod_cost):
    profit = sales - cost
    print("Total Profit", profit)

    # Total Profit 5200.0
    # Total Profit 5100.0
    # Total Profit 4800.0

