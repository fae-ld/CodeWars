# https://www.codewars.com/kata/517abf86da9663f1d2000003/

# Convert string to camel case -- CodeWars -- 6kyu
#
# Complete the method/function so that it converts dash/underscore delimited words
# into camel casing. The first word within the output should be capitalized
# only if the original word was capitalized (known as Upper Camel Case,
# also often referred to as Pascal case).
#
# Examples
# "the-stealth-warrior" gets converted to "theStealthWarrior"
# "The_Stealth_Warrior" gets converted to "TheStealthWarrior"

def to_camel_case(text):
    li, arr = list(text), []
    for i in range(len(li)):
        if '_' in li[i] or '-' in li[i]:
            li[i+1] = li[i+1].upper()
            pass
        else: arr.append(li[i])
    return ''.join(arr)