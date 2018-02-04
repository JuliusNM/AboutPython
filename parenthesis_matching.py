text = '((0.0)))'
istart = []  # stack of indices of opening parentheses
d = {}

for i, c in enumerate(text):
    if c == '(':
        istart.append(i)
    if c == ')':
        try:
            d[istart.pop()] = i
        except IndexError:
            print('Too many closing parentheses')
if istart:  # check if stack is empty afterwards
    print('Too many opening parentheses')

print(d)
