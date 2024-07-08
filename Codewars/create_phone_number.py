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

    number = ''.join(str(number) for number in n)
    return number


print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))


"""
best practice:
"""


def create_phone_number(n):
    return '({}{}{}) {}{}{}-{}{}{}{}'.format(*n)


print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))  # Output: "(123) 456-7890"
