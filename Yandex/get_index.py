import sys


def find_element_index_in_ordered_list(desired_element, ordered_list):
    result = 0
    for index, item in enumerate(ordered_list):
        if int(item) < desired_element:
            result += 1
            continue
        if int(item) == desired_element:
            return index
    return result


def main():
    ordered_list = sys.stdin.readline().rstrip().split()
    desired_element = int(sys.stdin.readline().rstrip())
    output_index = find_element_index_in_ordered_list(
        desired_element,
        ordered_list
    )

    print(output_index)


if __name__ == '__main__':
    main()
