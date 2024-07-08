def enigma(code: str) -> str:
    """Рассшифровываем полученые короткие сообщения.
    
    Параметры ввода:
    На вход принимаем защифрованную строку.
    Возвращаем:
    Расшифрованное сообщение в строке.
    """
    if len(code) <= 1:
        return code
    
    stack: list = []
    string: str = ""
    i: int = 0

    while i < len(code):
        if code[i].isdigit():
            count = 0
            if i < len(code) and code[i].isdigit():
                count = count * 10 + int(code[i])
                i += 1
            stack.append(count)
            
        elif code[i] == '[':
            stack.append(string)
            string = ""
            i += 1
            
        elif code[i] == ']':
            temp = stack.pop()
            counter = stack.pop()
            string = temp + counter * string
            i += 1
            
        else:
            string += code[i]
            i += 1

    return string


if __name__ == '__main__':
    code = input(str())
    print(enigma(code))