def check_duplicates(a):

    if len(a) != len(set(a)):
        print "Contains Duplicates"
    else:
        print "Does not contain Duplicates"

check_duplicates([1, 2, 4, 7, 7, 8, 5])

