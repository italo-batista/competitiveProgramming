import sys
sys.path.append('./datastructures')
from datastructures import Tree, BinaryTree, TreeNode


# Trre with Minimal Height -> number of nodes in the left subtree approximately equals to
# number of nodes in the right subtree.

def get_mid_index(array):
    if len(array) % 2 == 0:
        return int((len(array) / 2))
    else:
        return int(len(array) / 2)


def _minimal_height(array, btree):
    if len(array) == 0:
        return
    else:
        mid_index = get_mid_index(array)
        node = TreeNode(value=array[mid_index])

        if node.visited:
            return
        else:
            node.visited = True
            btree.insert(node)
            slice_right = array[:mid_index] if len(array) > 1 else []
            _minimal_height(slice_right, btree)
            slice_left = array[mid_index+1:] if len(array) > 1 else []
            _minimal_height(slice_left, btree)


def minimal_height(sorted_array):
    mid_index = get_mid_index(sorted_array)
    root = TreeNode(value=sorted_array[mid_index])
    btree = BinaryTree(root)

    _minimal_height(sorted_array[:mid_index], btree)
    shift_factor = 1 if len(sorted_array) > 1 else 0
    _minimal_height(sorted_array[mid_index+shift_factor:], btree)

    return btree


if __name__ == '__main__':  # tests

    sorted_array = [5, 10, 15, 20, 27, 30, 45, 90, 100, 110, 115, 120]
    btree = minimal_height(sorted_array)

    def visit(lista):
        def _visit(node):
            lista.append(node)

        return _visit

    result = []
    Tree.visit_in_order(btree.root, visit(result))
    result = list(map(lambda node: node.value, result))
    assert result == sorted_array
