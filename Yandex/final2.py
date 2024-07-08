# ID ???


def decode(data: str) -> str:
    '''
    Расшифровывает сжатые сообщения и возвращает строку с командами.
    '''
    result, current, count = "", "", 1

    for i, s in enumerate(data):
        if s.isdigit():
            count = int(s)
            current = ""

            continue

        if s == '[':
            left = i + 1
            print(left)

        if s.isalpha():
            current += s
            print(f'current {current}')

        if s == ']':
            right = i
            print(right)
            if '[' in data[left:right] and ']' not in data[left:right]:
                continue

            result += count * current
            current = ""

    return result


if __name__ == '__main__':
    data = input()
    print(decode(data))

# 3[a]2[bc]
# 3[a2[c]]
# 2[abc]3[cd]ef

# 3 * ('a') + 2 * ('bc'),
# 3 * ('a' + 2 * ('c')),
# 2 * ('abc') + 3 * ('cd') + 'ef'
