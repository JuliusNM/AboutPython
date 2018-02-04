with open("/home/julius/Desktop/ebooks/python_interview/pythonQnA.pdf") as fn:

    count = sum(character.isupper() for line in fn for character in line)
    print(count)
