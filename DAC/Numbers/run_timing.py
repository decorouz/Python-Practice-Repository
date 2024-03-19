def run_timing():
    """Asks the user repeatedly for numeric input. Prints the average time and number of runs."""

    num_of_runs = 0
    total_time = 0

    while True:

        try:
            one_run = input("Enter 10 km run time: ")
            if not one_run:
                break

            num_of_runs += 1
            total_time += float(one_run)

            average_time = total_time / num_of_runs
            print(f'Average of {average_time:.2f}, over {num_of_runs} runs')
        except ValueError as e:
            print("That's not a valid number! Please enter a valid numeric input!")


run_timing()
