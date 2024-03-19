def url_encode_characters(string_: str):
    """
    Given a string, URL-encode any character that isn’t a letter
    or number. For the purposes of this exercise, we’ll assume that all characters are indeed in ASCII (i.e., one byte long), and not multibyte UTF-8 characters. It might help to know about the ord.
    """
    return "".join("%{0:0>2}".format(format(ord(char), "x")) for char in string_)


print(
    url_encode_characters(
        "https://stackoverflow.com/questions/67629248/how-do i urlencode"
    )
)
