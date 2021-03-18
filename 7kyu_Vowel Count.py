# https://www.codewars.com/kata/54ff3102c1bad923760001f3/train/python

# Return the number (count) of vowels in the given string.
#
# We will consider a, e, i, o, u as vowels for this Kata (but not y).
#
# The input string will only consist of lower case letters and/or spaces.

def get_count(input_str):
    vowel, sum, str = ['a','i','u','e','o'], 0, list(input_str)
    for i in vowel:
        for j in range(len(str)):
            if i in str[j]:
                sum += 1
    return sum

