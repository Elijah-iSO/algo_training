# ID 103316300


def decode(data: str) -> str:
    '''
    Расшифровывает сжатые сообщения в формате "2[с]3[в]ш",
    где цифры количество повторений, буквы - обозначение команды.
    Возвращает строку с командами в формате "ссвввш".
    Формат ввода: Гарантированно приходит валидная строка.
    В строке могут быть только буквы, числа и квадратные скобки.
    Длина строки может находиться в диапазоне от 0 (пустая строка)
    до 30 символов включительно.
    Числа в строке могут быть от 1 до 300 включительно.
    '''
    result, m_stack, stack, mult = '', [], [], 0

    for simbol in data:

        if simbol.isdigit():
            mult = 10 * mult + int(simbol)
            m_stack.append(mult)

        elif simbol == '[':
            mult = 0
            stack.append(result)
            result = ''

        elif simbol.isalpha():
            result += simbol

        elif simbol == ']':
            previos = stack.pop()
            stack.append(result * m_stack.pop())
            result = previos + stack.pop()

    return result


if __name__ == '__main__':
    data = input()
    print(decode(data))
