# https://www.codewars.com/kata/52597aa56021e91c93000cb0/train/python

# Moving zeros to the end -- Codewars -- 5kyu
# Write an algorithm that takes an array and moves all of the zeros to the end,
# preserving the order of the other elements.
# move_zeros([1, 0, 1, 2, 0, 1, 3]) ==>> returns [1, 1, 2, 1, 3, 0, 0]
def move_zeros(arr):
    new_arr, zero = [], []
    for i in arr:
        if i == 0:
            zero.append(i)
        else:
            new_arr.append(i)

    return new_arr + zero
