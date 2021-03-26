# https://www.codewars.com/kata/5208f99aee097e6552000148/

# Break camelCase -- CodeWars -- 6kyu
# Complete the solution so that the function will break up camel casing,
# using a space between words.
#
# Example
# solution("camelCasing")  ==  "camel Casing"

def solution(s):
    li = list(s)
    for i in range(len(li)):
        if li[i].isupper(): li[i] = ' {}'.format(li[i])
    return ''.join(li)