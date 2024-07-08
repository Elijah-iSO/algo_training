def is_correct_bracket_seq(data):
    result = []
    for i in data:
        if i in '([{':
            result.append(i)
        else:
            if result:
                if i == ')' and result[-1] == '(':
                    result.remove('(')

                elif i == ']' and result[-1] == '[':
                    result.remove('[')

                elif i == '}' and result[-1] == '{':
                    result.remove('{')

                else:
                    return False

            else:
                return False

    return True


if __name__ == '__main__':
    data = input()
    print(is_correct_bracket_seq(data))

assert is_correct_bracket_seq('{[()]}') is True
assert is_correct_bracket_seq('()') is True
assert is_correct_bracket_seq('') is True
assert is_correct_bracket_seq('({[]})([])') is True
assert is_correct_bracket_seq(')(') is False
assert is_correct_bracket_seq('([)]') is False
assert is_correct_bracket_seq('({]})') is False
assert is_correct_bracket_seq('((())])') is False
