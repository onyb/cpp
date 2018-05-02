def longest_substring(s):
    start = end = 0
    longest = ''
    pool = set()

    while end < len(s):
        char = s[end]

        if char not in pool:
            pool.add(char)

            if len(s[start:end+1]) > len(longest):
                longest = s[start:end+1]

            end += 1
            continue

        while start < end and s[start] != char:
            pool.remove(s[start])
            start += 1

        start += 1
        end += 1

    return longest


result = longest_substring('')
assert result == '', result

result = longest_substring('ABCBDX')
assert result == 'CBDX', result
