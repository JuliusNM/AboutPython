def LetterChanges(word):

    zabc = 'abcdefghijklmonpqrstuvwxyz'
    ab_st = list(zabc)
    new_word = []
    for letter in list(word.lower()):
        new_word.append(ab_st[zabc.index(letter) + 1])
    new_word = "".join(new_word)
    return new_word

print(LetterChanges("abc"))
