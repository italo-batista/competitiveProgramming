

class GraphNode:
    def __init__(self, value=None, adjacents=None):
        # type (any, list)

        self.value = value
        self.visited = False
        self.adjacents = adjacents if adjacents else []

    def add_adj(self, adj):
        self.adjacents.append(adj)


class TreeNode:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None
        self.visited = False


class Tree(object):
    def __init__(self, root):  # type (TreeNode)
        self.root = root

    @classmethod
    def visit_in_order(cls, tree_node, visit_function):
        # type (class, TreeNode, function(TreeNode)
        if tree_node:
            Tree.visit_in_order(tree_node.left, visit_function)
            visit_function(tree_node)
            Tree.visit_in_order(tree_node.right, visit_function)


    @classmethod
    def visit_pre_order(cls, tree_node, visit_function):
        # type (class, TreeNode, function(TreeNode)
        if tree_node:
            visit_function(tree_node)
            Tree.visit_pre_order(tree_node.left, visit_function)
            Tree.visit_pre_order(tree_node.right, visit_function)


    @classmethod
    def visit_post_order(cls, tree_node, visit_function):
        # type (class, TreeNode, function(TreeNode)
        if tree_node:
            Tree.visit_post_order(tree_node.left, visit_function)
            Tree.visit_post_order(tree_node.right, visit_function)
            visit_function(tree_node)


class BinaryTree(Tree):

    def __init__(self, root):  # type (TreeNode)
        super(BinaryTree, self).__init__(root)

    def insert(self, node):  # type (TreeNode)
        if not self.root:
            self.root = node
        else:
            curr_node = self.root
            while curr_node:
                if node.value < curr_node.value:
                    if curr_node.left is None:
                        curr_node.left = node
                        curr_node = None
                    else:
                        curr_node = curr_node.left
                elif node.value >= curr_node.value:
                    if curr_node.right is None:
                        curr_node.right = node
                        curr_node = None
                    else:
                        curr_node = curr_node.right
