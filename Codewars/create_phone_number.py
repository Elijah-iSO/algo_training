"""
Write a function that accepts an array of 10 integers (between 0 and 9),
that returns a string of those numbers in the form of a phone number.

Example
create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
"""


def create_phone_number(n):
    for index in range(len(n)):
        if index == 1:
            n.insert(0, '(')
        elif index == 4:
            n.insert(4, ') ')
        elif index == 8:
            n.insert(8, '-')
        else:
            continue

    return ''.join(str(number) for number in n)


"""
best practice:
"""


def create_phone_number1(n):
    return '({}{}{}) {}{}{}-{}{}{}{}'.format(*n)


def create_phone_number2(n):
    n = ''.join(map(str, n))
    return '(%s) %s-%s'%(n[:3], n[3:6], n[6:])


print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
print(create_phone_number1([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
print(create_phone_number2([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
