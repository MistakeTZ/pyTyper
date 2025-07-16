import re

def replace_html_tags(text: str):
    return text.replace("<", "&lt;").replace(">", "&gt;")


def get_token_at(s: str, index: int):
    for match in re.finditer(r'\w+|[.,()]', s):
        start, end = match.start(), match.end()
        if start <= index < end:
            return match.group()
    return None


def sql_checker(line: str, index: int, input_char: str) -> bool:
    token = get_token_at(line, index)
    if token and token.isupper():
        return line[index].lower() == input_char.lower()
    return False
