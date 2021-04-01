# https://www.codewars.com/kata/598ee7b6ec6cb90dd6000061/

# Count Repeats -- CodeWars -- 6kyu
# Write a function that returns the count of characters that have to be removed
# in order to get a string with no consecutive repeats.
#
# Note: This includes any characters
#
# Examples
# 'abbbbc'  => 'abc'    #  answer: 3
# 'abbcca'  => 'abca'   #  answer: 2
# 'ab cca'  => 'ab ca'  #  answer: 1

def count_repeats(txt):
    li, c = list(txt), 0
    for i in range(1,len(li)):
        if li[i] == li[i-1]: c += 1
    return c