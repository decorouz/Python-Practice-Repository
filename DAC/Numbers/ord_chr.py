
def ord_chr():

    decnum = 0
    hexnum = input("Enter a hex number to convert: ")

    for power, digit in enumerate(reversed(hexnum)):
        if 48 <= ord(digit) <= 57:
            dec_digit = ord(digit) - 48
        elif 97 <= ord(digit) <= 102:
            dec_digit = ord(digit) - 87
        decnum += dec_digit * (16**power)
    print(decnum)


ord_chr()
