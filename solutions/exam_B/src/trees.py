class Node:
    """A node of a binary tree. A missing child is None."""

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# Complexity of all of them: every node is visited once -> O(n), n = number
# of nodes (is_bst too). The recursion depth is the height of the tree.

# 1 : base case = empty tree (None) -> 0. Otherwise 1 + the taller child.
def height(node):
    if node is None:
        return 0
    return 1 + max(height(node.left), height(node.right))


# 2 : a leaf has no child at all -> counts 1; otherwise sum over the children.
def count_leaves(node):
    if node is None:
        return 0
    if node.left is None and node.right is None:
        return 1
    return count_leaves(node.left) + count_leaves(node.right)


# 3 : value of the node + sum of the two children.
def tree_sum(node):
    if node is None:
        return 0
    return node.value + tree_sum(node.left) + tree_sum(node.right)


# 4 : NOT a BST, so both children may hold the value. `or` stops as soon as
# one side is True.
def contains(node, value):
    if node is None:
        return False
    return node.value == value or contains(node.left, value) or contains(node.right, value)


# 5 : infix = left, node, right.
def collect_infix(node):
    if node is None:
        return []
    return collect_infix(node.left) + [node.value] + collect_infix(node.right)


# 6 : every value must be in the open interval (low, high); going left, the
# node's value becomes the new upper bound; going right, the new lower bound.
# None = no bound.
def is_bst(node, low=None, high=None):
    if node is None:
        return True
    if low is not None and node.value <= low:
        return False
    if high is not None and node.value >= high:
        return False
    return is_bst(node.left, low, node.value) and is_bst(node.right, node.value, high)
