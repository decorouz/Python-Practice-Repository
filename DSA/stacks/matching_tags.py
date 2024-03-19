"""Application of matching delimiters is in the validation of makeup
languages such as HTML.

For example a simple opening HTML tag has the form '<name>' and 
the corresponding closing tag as the form '</name>'
"""

from main import ArrayStack


def is_matched_html(raw_html):
    """Return True if all HTML tags are properly match; False otherwise."""
    S = ArrayStack()
    # find the first '<' character (if any)
    j = raw_html.find("<")

    while j != -1:
        k = raw_html.find(">", j + 1)  # find the next ">" character
        if k == -1:
            return False  # Invalid tag
        tag = raw_html[j + 1 : k]  # strip away < >
        if not tag.startswith("/"):  # this is opening tag
            S.push(tag)
        else:  # this is closing tag
            if S.is_empty():
                return False  # nothing to match with
            if tag[1:] != S.pop():
                return False  # mismatched delimiter
        j = raw_html.find("<", k + 1)  # find next '<' character
    return S.is_empty()  # were all opening tags matched


if __name__ == "__main__":
    raw = "<name> some text </name>"
    print(is_matched_html(raw))
