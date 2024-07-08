from __future__ import annotations


class TreeNode:

    def __init__(self, p, a, c):
        self.p = p  # уровень родительской вершины, от корня 0.
        self.a = a  # стоимость акций
        self.c = c  # наименование компании


class TotalPrice:

    def __init__(self, treenode: TreeNode):
        self.parent = treenode
        self.total_price = 0

    def count_sum(self):
        self.total_price += self.parent.a

        return self.total_price


# кол-во вершин, кол-во компаний
n, k = 5, 2
companies = ['A', 'B']  # названия компаний
# вершины: родитель, стоимость акций, название компании
nodes = (
    (0, 1, 'A'),
    (1, 2, 'A'),
    (1, 2, 'B'),
    (1, 1, 'B'),
    (4, 2, 'A'),
)

tree_nodes = {}

for i in range(n):
    tree_nodes[i] = nodes[i]

print(tree_nodes)
