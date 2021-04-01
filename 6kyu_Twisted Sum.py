# https://www.codewars.com/kata/527e4141bb2ea5ea4f00072f

# Twisted Sum -- CodeWars -- 6kyu
# Find the sum of the digits of all the numbers from 1 to N (both ends included).

# Examples
# # N = 4
# 1 + 2 + 3 + 4 = 10

# # N = 10
# 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + (1 + 0) = 46

# # N = 12
# 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + (1 + 0) + (1 + 1) + (1 + 2) = 51

def compute_sum(n):
    c = 0
    for i in range(n+1):
        strin = str(i)
        if len(strin) >= 2:
            for j in strin: c += int(j)
        else: c+=i
    return c

# or you can try:

def compute_sum(n):
    return sum(int(c) for i in range(1, n+1) for c in str(i))