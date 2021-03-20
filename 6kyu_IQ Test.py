# https://www.codewars.com/kata/552c028c030765286c00007d/

# Bob is preparing to pass IQ test.
# The most frequent task in this test is to find out which one of
# the given numbers differs from the others. Bob observed that one number usually
# differs from the others in evenness. Help Bob — to check his answers,
# he needs a program that among the given numbers finds one that is different in evenness,
# and return a position of this number.
#
# ! Keep in mind that your task is to help Bob solve a real IQ test,
# which means indexes of the elements start from 1 (not 0)
#
# Examples:
# iq_test("2 4 7 8 10") => 3 # Third number is odd, while the rest of the numbers are even
#
# iq_test("1 2 1 1") => 2 # Second number is even, while the rest of the numbers are odd

def iq_test(numbers):
    num, odd, even = numbers.split(' '), [], []
    numba = list(num)
    for i in range(len(numba)): num[i] = int(num[i])
    for j in range(len(numba)):
        if num[j]%2==0: even.append(num[j])
        else: odd.append(num[j])

    return num.index(odd[0]) + 1 if len(odd)<len(even) else num.index(even[0]) + 1
