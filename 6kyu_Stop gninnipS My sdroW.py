# https://www.codewars.com/kata/5264d2b162488dc400000001/

# Stop gninnipS My sdroW -- CodeWars -- 6kyu
# Write a function that takes in a string of one or more words,
# and returns the same string, but with all five or more letter words reversed
# (Just like the name of this Kata). Strings passed in will consist of only letters and spaces.
# Spaces will be included only when more than one word is present.
#
# Examples:
#
# spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw"
#
# spinWords( "This is a test") => returns "This is a test"
#
# spinWords( "This is another test" )=> returns "This is rehtona test"
def spin_words(sentence):
    li = sentence.split(' ')
    for i in range(len(li)):
        if len(li[i]) >= 5: li[i] = li[i][::-1]
    return ' '.join(li)

# or you can try :

#def spin_words(sentence):
#   return " ".join([x[::-1] if len(x) >= 5 else x for x in sentence.split(" ")])