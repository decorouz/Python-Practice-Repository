def mean(num_list):
    """Accept a non-empty  list of numbers. 
    Return the average of those numbers"""
    try:
        return sum(num_list)/len(num_list)
    except ZeroDivisionError as e:
        return str(e)


print(mean([10, 20, 30, 40]))
