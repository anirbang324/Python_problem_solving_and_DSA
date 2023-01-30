import re


def remove(s):
    gp = [match.group() for match in re.finditer(r'(.)\1*', s)]
    s = ''
    for i in gp:
        if len(i) > 1:
            continue
        s += i
    return s


def rremove(s):
    ps = ''
    while len(ps) != len(s):
        ps = s
        s = remove(s)
    return s

str1 = input()
print(rremove(str1))
