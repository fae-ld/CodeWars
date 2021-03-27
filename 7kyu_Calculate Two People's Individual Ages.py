# https://www.codewars.com/kata/58e0bd6a79716b7fcf0013b1/

# Calculate Two People's Individual Ages -- CodeWars -- 7kyu
# Create a function that takes in the sum and age difference of two people,
# calculates their individual ages, and returns a pair of values (oldest age first)
# if those exist or null/None if:
#
# sum < 0
# difference < 0
# Either of the calculated ages come out to be negative


def get_ages(sum_, diff):
    arr = [(sum_+diff)/2, (sum_-diff)/2]
    return tuple(arr) if min(arr) >= 0 and (sum_ >= 0 and diff >= 0) else None
