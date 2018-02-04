def remove_duplicates(string):
    word_set = "".join(sorted(set(string)))
    if word_set:
        return (word_set, len(string)-len(word_set))
print(remove_duplicates("helllloooo"))