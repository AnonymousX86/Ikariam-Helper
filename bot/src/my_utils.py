import re
import os


def strip_emoji(text):
    re_emoji = re.compile(u'([\U00002600-\U000027BF])|([\U0001f300-\U0001f64F])|([\U0001f680-\U0001f6FF])')
    return re_emoji.sub(r'', text)


def fixed_width(text: str, width: int = 20):
    text = strip_emoji(text)
    if text:
        if len(text) == width:
            return text
        elif len(text) > width:
            return text[:width-3] + '...'
        else:
            while len(text) < width:
                text += ' '
            return text
    else:
        raise SyntaxError('No text')


def separate(value, separator=' '):
    result = ''
    for c in range(1, len(n := str(value)) + 1):
        result += n[-c]
        if c % 3 == 0:
            result += separator
    return result[::-1]


def upper_name(name):
    if ' ' not in name:
        return f'{name[0].upper()}{name[1:]}'
    else:
        result = ''
        i = 0
        while True:
            if i >= len(name):
                return result
            elif i == 0:
                result += name[0].upper()
                i += 1
            elif name[i] == ' ':
                result += name[i:i + 2].upper()
                i += 2
            else:
                result += name[i]
                i += 1


def get_database(name: str):
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
    return os.path.join(__location__, f'../src/{name}.sqlite')


def sort_nested_list(nested_list: list):
    nested_list.sort(key=lambda x: x[0].lower())
    return nested_list
