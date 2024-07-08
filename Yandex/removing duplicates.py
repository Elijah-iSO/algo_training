import sys


def find_duplicate(ordered_list):
    result = []
    _list = []
    for item in ordered_list:
        if item not in result:
            result.append(item)
        else:
            _list.append('_')
    print(result+_list)
    return result+_list


def main():
    list_length = int(sys.stdin.readline().rstrip())
    ordered_list = sys.stdin.readline().rstrip().split()
    output_numbers = find_duplicate(ordered_list)

    print(' '.join(output_numbers))


if __name__ == '__main__':
    main()
