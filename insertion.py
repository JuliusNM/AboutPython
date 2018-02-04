def insertion(alist):
    for index in range(1, len(alist)):

        current_value = alist[index]
        position = index

        while position > 0 and alist[position - 1] > current_value:
            alist[position] = alist[position - 1]
            position -= 1
        alist[position] = current_value

alisted = [1, 4, 6, 8, 3, 9]
insertion(alisted)
print(alisted)
