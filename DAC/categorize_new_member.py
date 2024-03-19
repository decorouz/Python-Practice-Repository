input = [[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]


# My initial solution
def open_or_senior(data):
    output = []
    for item in data:
        if item[0] >= 55 and item[-1] > 7:
            output.append("Senior")
        else:
            output.append("Open")
    return output


# My refactored Solution
def open_or_senior(data):
    return ["Senior" if age >= 55 and handicap >= 8 else "Open" for (age, handicap) in data]


print(open_or_senior(input))
