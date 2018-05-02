import re

def atoi(str):
    """
    :type str: str
    :rtype: int
    """
    regex = r'\s*(?P<sign>[-+]?)(?P<integer>\d+).*'
    m = re.match(regex, str)

    if not m:
        return 0

    integer, sign = int(m.group('integer')), m.group('sign')
    result = integer * -1 if sign == '-' else integer

    INT_MAX = 2**31 - 1
    INT_MIN = -(2**31)

    if result < INT_MIN:
        return INT_MIN
    elif result > INT_MAX:
        return INT_MAX
    else:
        return result


assert atoi('42') == 42
assert atoi('   -42') == -42
assert atoi('4193 with words') == 4193
assert atoi('words and 987') == 0
assert atoi('-91283472332') == -2147483648
