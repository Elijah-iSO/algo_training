from array import array


def valid_mountain_array(data_array):
    max_height = max(data_array)
    max_height_index = data_array.index(max_height)
    if len(data_array) < 3 or data_array.count(max_height) > 1:
        return False
    try:
        for index, value in enumerate(data_array):
            if index < max_height_index and value >= data_array[index+1]:
                return False
            if index > max_height_index and value <= data_array[index+1]:
                return False
            if data_array[0] >= max_height or data_array[-1] >= max_height:
                return False
    except IndexError:
        pass
    return True


def main():
    data_array = array('b', map(int, input().split()))
    print(valid_mountain_array(data_array))


if __name__ == '__main__':
    main()
