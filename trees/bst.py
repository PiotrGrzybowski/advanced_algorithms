from typing import TypeVar, List

T = TypeVar('T')


class Node:
    def __init__(self, value: T, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f'Node({self.value})'


def search(root: Node, value: T):
    if root is None or root.value == value:
        return root
    elif root.value < value:
        return search(root.right, value)
    else:
        return search(root.left, value)


def count_nodes(root: Node):
    if root is None:
        return 0
    else:
        return 1 + count_nodes(root.left) + count_nodes(root.right)


def count_depth(root: Node):
    if root is None:
        return 0
    else:
        return 1 + max(count_depth(root.left), count_depth(root.right))


def insert(root: Node, value):
    if root is None:
        return Node(value)

    if value > root.value:
        root.right = insert(root.right, value)
    else:
        root.left = insert(root.left, value)

    return root


def has_path_sum(root: Node, target: int):
    def has_path_hum_help(node: Node, accum: int):
        if node.left and node.right:
            return has_path_hum_help(node.left, accum + node.value) or has_path_hum_help(node.right, accum + node.value)
        elif node.left:
            return has_path_hum_help(node.left, accum + node.value)
        elif node.right:
            return has_path_hum_help(node.right, accum + node.value)
        else:
            return accum + node.value == target

    if root:
        return has_path_hum_help(root, 0)
    else:
        return False


def has_path_sum_2(root: Node, target: int):
    def has_path_hum_help(node: Node, accum: List[int]):
        if node.left and node.right:
            return has_path_hum_help(node.left, accum + [node.value]) or has_path_hum_help(node.right,
                                                                                           accum + [node.value])
        elif node.left:
            return has_path_hum_help(node.left, accum + [node.value])
        elif node.right:
            return has_path_hum_help(node.right, accum + [node.value])
        else:
            if sum(accum) + node.value == target:
                return accum + [node.value]
            else:
                return []

    if root:
        return has_path_hum_help(root, [])
    else:
        return False


def count_outer_leaves(root: Node):
    if root is None:
        return 1
    else:
        return count_outer_leaves(root.left) + count_outer_leaves(root.right)


if __name__ == '__main__':
    root = None
    root = insert(root, 15)
    root = insert(root, 9)
    root = insert(root, 6)
    root = insert(root, 10)
    root = insert(root, 7)
    root = insert(root, 3)
    root = insert(root, 4)
    root = insert(root, 17)

    print(count_outer_leaves(root))
    # print()
