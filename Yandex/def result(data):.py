def result(data):
    output = []
    for i in data:
        output.insert(0, i)

    return output


if __name__ == '__main__':
    data = input()
    print(result(data))
