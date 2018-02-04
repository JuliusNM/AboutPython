def recurring_char(given_string):

    counts = {}
    for char in given_string:
        if char in counts:
            print(char, counts)
        else:
            counts[char] = 1
recurring_char("Helelo")
