# https://www.codewars.com/kata/5748838ce2fab90b86001b1a

# Complete the function that calculates the area of the red square, when the length of the circular arc A is given as the input. Return the result rounded to two decimals.
#
# Graph
#
# Note: use the π value provided in your language (Math::PI, M_PI, math.pi, etc)

from math import pi
def square_area(A):
    r = ((4*A)/pi)/2
    return round(r**2, 2)

# or you can do :
# from math import pi
# def square_area(a):
#     return round(((((4*a)/pi)/2)**2),2)