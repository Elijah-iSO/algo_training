# ID 102472357

def platforms_count(data: list[int], limit: int) -> int:
    '''
    Вычисляет минимальное количество необходимых платформ
    для транспортировки роботов, вес которых передается в data,
    а ограничение по весу на одну платформу - в limit.
    '''
    platforms_count, left_pointer, right_pointer = 0, 0, len(data) - 1

    while left_pointer < right_pointer:
        result = data[left_pointer] + data[right_pointer]
        platforms_count += 1
        right_pointer -= 1

        if result <= limit:
            left_pointer += 1

    if left_pointer == right_pointer:
        platforms_count += 1
    return platforms_count


if __name__ == '__main__':
    data = sorted([int(i) for i in input().split()])
    limit = int(input())
    print(platforms_count(data, limit))
