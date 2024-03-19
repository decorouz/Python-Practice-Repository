from unicodedata import name


def name_triangle():
    """Get the user name. Print a name triangle. starting 
    with the first letter, then the first two letters and then the first three letters"""

    name = input("Enter your name: ")
    for i in range(len(name)):
        print(name[:i+1])


name_triangle()
