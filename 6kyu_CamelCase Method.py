# https://www.codewars.com/kata/587731fda577b3d1b0001196/solutions/python

# CamelCase Method -- CodeWars -- 6kyu

# Write simple .camelCase method (camel_case function in PHP,
# CamelCase in C# or camelCase in Java) for strings.
# All words must have their first letter capitalized without spaces.
#
# For instance:
#
# camelcase("hello case") => HelloCase
# camelcase("camel case word") => CamelCaseWord
# Don't forget to rate this kata! Thanks :)

def camel_case(text):
    txt, indx, x = list(text), [], 0
    for i in range(len(txt) - 1):  # split + check
        txt[0] = txt[0].upper()  # y'know what is this
        if ' ' in txt[i]: txt[i + 1] = txt[i + 1].upper()  # if ' ', then the (value+1) must be uppercase

    for j in range(len(txt) - 1):  # finding for the index value of txt containing ' ' (space)
        if ' ' in txt[j]: indx.append(j)

    for a in range(len(indx)): del txt[indx[a] - a]  # delete list value with ' ' (space)

    for x in range(len(txt)):  # checking for the last time
        if ' ' in txt[x]: del txt[x]  # if still contains ' ' then it will be deleted

    return ''.join(txt)

# or you can do :

# return string.title().replace(" ", "")

# hehe :)