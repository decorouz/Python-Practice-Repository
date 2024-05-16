"""Write a function txt2morse, which translates a text to "morse" code, 
i.e. the function returns a string with the morse code.
Write another function morse2txt which translates a string in Morse code into a "normal“ string.
The Morse character are separated by spaces. Words by three spaces.
"""

# International Morse code
# The length of a dot is one unit
# A dash is 3 units
# The space between parts of the same letter is one unit
# The space between letters is 3 units
# The space between words is seven units.

# fmt: off
latin2morse_dict = {'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 
                    'E':'.', 'F':'..-.', 'G':'--.','H':'....', 
                    'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..', 
                    'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 
                    'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-', 
                    'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 
                    'Y':'-.--', 'Z':'--..', '1':'.----', '2':'...--', 
                    '3':'...--', '4':'....-', '5':'.....', '6':'-....', 
                    '7':'--...', '8':'---..', '9':'----.', '0':'-----', 
                    ',':'--..--', '.':'.-.-.-', '?':'..--..', ';':'-.-.-', 
                    ':':'---...', '/':'-..-.', '-':'-....-', '\'':'.----.', 
                    '(':'-.--.-', ')':'-.--.-', '[':'-.--.-', ']':'-.--.-', 
                    '{':'-.--.-', '}':'-.--.-', '_':'..--.-'}

# Reverse the dictionary

morse2latin_dict = dict(zip(latin2morse_dict.values(), latin2morse_dict.keys()))


def txt2morse(txt: str, alphabet:dict) -> str:
    morse_code = ""
    for char in txt.upper():
        if char == " ":
            morse_code += "   " # The space between letters is 3 units
        else:
            morse_code += alphabet[char] + " " #The space between parts of the same letter is one unit
    return morse_code


def morse2txt(txt: str, alphabet: dict) -> str:
    res= ""
    morse_words = txt.split("   ")
    for mword in morse_words:
        for mchar in mword.split():
            res += alphabet[mchar]
        res += " "
    return res
        

# Text the implementation
if __name__ == "__main__":
    text = "So what?"
    morse_string = txt2morse(text, alphabet=latin2morse_dict)
    moorse2txt = morse2txt(morse_string, alphabet=morse2latin_dict)
    print(morse_string)
    print(moorse2txt)
