import re

tmpLink1 = "https://b-ok.asia/book/2957207/47b46d?dsource=mostpopular"

def use_regex(input_text):
    pattern = re.compile(r"\?[a-zA-Z]+=[a-zA-Z]+", re.IGNORECASE)
    return pattern.match(input_text)

print(use_regex(tmpLink1))
