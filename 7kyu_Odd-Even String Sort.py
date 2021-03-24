# https://www.codewars.com/kata/580755730b5a77650500010c/

# Odd-Even String Sort -- CodeWars -- 7kyu
# Given a string S. You have to return another string such
# that even-indexed and odd-indexed characters of S are grouped and
# groups are space-separated (see sample below)
#
# Note:
# 0 is considered to be an even index.
# All input strings are valid with no spaces
# input: 'CodeWars'
# output 'CdWr oeas'
#
# S[0] = 'C'
# S[1] = 'o'
# S[2] = 'd'
# S[3] = 'e'
# S[4] = 'W'
# S[5] = 'a'
# S[6] = 'r'
# S[7] = 's'
# Even indices 0, 2, 4, 6, so we have 'CdWr' as the first group
# odd ones are 1, 3, 5, 7, so the second group is 'oeas'
# And the final string to return is 'Cdwr oeas'
#
# Enjoy.

def sort_my_string(S):
    li, arr0, arr1 = list(S), [], []
    for i in range(len(li)):
        if i%2==0: arr0.append(li[i])
        else: arr1.append(li[i])
    arr0.append(' ')
    return ''.join(arr0 + arr1)