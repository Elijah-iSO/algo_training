# Импорт модуля os из стандартной библиотеки 
# для взаимодействия с операционной системой.
import os

# Считывание переменной окружения REMOTE_JUDGE, чтобы определить, 
# локально выполняется код или на удалённом сервере.
LOCAL = os.environ.get('REMOTE_JUDGE', 'false') != 'true'

# Если код выполняется на локальном компьютере, то...
if LOCAL:
    # Класс, описывающий элементы связного списка:
    class Node:
        def __init__(self, value, next_item=None):
            self.value = value
            self.next_item = next_item


def solution(node, idx):
    # Напишите код функции здесь.
    if node is None:
        return node

    if idx == 0:
        node = node.next_item
        return node

    list_items_count = 0
    curr = node
    prev = None

    while curr is not None and list_items_count != idx:
        prev = curr
        curr = curr.next_item
        list_items_count += 1

    if curr is None:
        return node

    prev.next_item = curr.next_item
    curr = None

    return node


# Тестирующая функция для проверки решения.
# Не изменяйте её, она не требует вашего внимания.
def test():
    node3 = Node("Задача 4: Обследовать грунт в радиусе 3 м", None)
    node2 = Node("Задача 3: Измерить температуру атмосферы", node3)
    node1 = Node("Задача 2: Пробурить скважину глубиной 0.5 м", node2)
    node0 = Node("Задача 1: Фотосъёмка 360°", node1)

    new_head = solution(node0, 1)
    assert new_head is node0
    assert new_head.next_item is node2
    assert new_head.next_item.next_item is node3
    assert new_head.next_item.next_item.next_item is None
    # result is node0 -> node2 -> node3


if __name__ == '__main__':
    test()
