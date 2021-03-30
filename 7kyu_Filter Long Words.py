# https://www.codewars.com/kata/5697fb83f41965761f000052/

# Filer Long Words -- CodeWars -- 7kyu
# Write a function filter_long_words that takes a string sentence and an integer n.
#
# Return a list of all words that are longer than n.
#
# Example:
#
# filter_long_words("The quick brown fox jumps over the lazy dog", 4) = ['quick', 'brown', 'jumps']

def filter_long_words(sentence, n):
    arr, li = [], sentence.split(' ')
    for i in range(len(li)):
        if len(li[i]) > n: arr.append(li[i])
    return arr

# or you can try : 
def filter_long_words(sentence, n):
    return [word for word in sentence.split() if len(word) > n]