def longest(word):
    if type(word) != str:
        raise TypeError("Input not a string")
    words = word.split()
    longest = max(words, key=len)
    return longest, len(longest)

print(longest("This is the day that the lord has made, Julius"))
