"""
BINARY TREES AND BINARY SEARCH TREES (BST)

Run:  python3 snippets/trees.py

=============================  THE ONE IDEA  =============================
A tree is either   None (empty)     or   a Node with a value, a left tree and a right tree.
So EVERY function has this shape:

    def f(node):
        if node is None:            # base case: what is the answer for the EMPTY tree?
            return <neutral value>  #   0 for sum/count/height, [] for lists, False for contains
        ... combine  node.value  with  f(node.left)  and  f(node.right)

RULES
 * test emptiness with `node is None`  (NOT `node = None`, NOT `node == None`).
 * leaf = a node with NO child:  node.left is None and node.right is None.
 * the time complexity of a "visit every node once" function is O(n), n = number of nodes.
 * build a list from a tree with `+` (concatenation) of the sub-results, never append(list).
 * the recursion depth is the HEIGHT: O(log n) for a balanced tree, O(n) for a degenerate one (a list).

Example tree used in the checks:         8
                                       /   \\
                                      3     10
                                     / \\      \\
                                    1   6      14
                                       / \\    /
                                      4   7  13
"""
from collections import deque


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f"Node({self.value})"


# ---------------------------------------------------------------------------------------------
# 1. MEASURES                                           all O(n)
# ---------------------------------------------------------------------------------------------
def size(node):
    if node is None:
        return 0
    return 1 + size(node.left) + size(node.right)


def height(node):
    """Number of NODES on the longest path (height(None) = 0, single node = 1)."""
    if node is None:
        return 0
    return 1 + max(height(node.left), height(node.right))


def count_leaves(node):
    if node is None:
        return 0
    if node.left is None and node.right is None:
        return 1
    return count_leaves(node.left) + count_leaves(node.right)


def tree_sum(node):
    if node is None:
        return 0
    return node.value + tree_sum(node.left) + tree_sum(node.right)


def tree_max(node):
    """Largest value (any tree). None for the empty tree."""
    if node is None:
        return None
    best = node.value
    for child in (node.left, node.right):
        child_best = tree_max(child)
        if child_best is not None and child_best > best:
            best = child_best
    return best


def count_internal(node):
    """Nodes that have at least one child."""
    if node is None or (node.left is None and node.right is None):
        return 0
    return 1 + count_internal(node.left) + count_internal(node.right)


def count_equal(node, value):
    if node is None:
        return 0
    return (1 if node.value == value else 0) + count_equal(node.left, value) + count_equal(node.right, value)


def contains(node, value):
    """Any tree (NOT a BST): look in both children. O(n)."""
    if node is None:
        return False
    return node.value == value or contains(node.left, value) or contains(node.right, value)


def depth_of(node, value, depth=0):
    """Depth (root = 0) of the first node holding value, or -1."""
    if node is None:
        return -1
    if node.value == value:
        return depth
    found = depth_of(node.left, value, depth + 1)
    if found != -1:
        return found
    return depth_of(node.right, value, depth + 1)


def is_balanced(node):
    """Heights of the two children differ by at most 1, at EVERY node. O(n^2) naive version."""
    if node is None:
        return True
    return (abs(height(node.left) - height(node.right)) <= 1
            and is_balanced(node.left) and is_balanced(node.right))


def same_tree(a, b):
    if a is None and b is None:
        return True
    if a is None or b is None:
        return False
    return a.value == b.value and same_tree(a.left, b.left) and same_tree(a.right, b.right)


def mirror(node):
    """New tree with left and right swapped everywhere."""
    if node is None:
        return None
    return Node(node.value, mirror(node.right), mirror(node.left))


# ---------------------------------------------------------------------------------------------
# 2. THE FOUR TRAVERSALS (return a list)                O(n)
#    prefix  : node, left, right      infix : left, node, right      postfix : left, right, node
#    BFS (by level) : a queue, not a recursion
# ---------------------------------------------------------------------------------------------
def prefix(node):
    if node is None:
        return []
    return [node.value] + prefix(node.left) + prefix(node.right)


def infix(node):
    if node is None:
        return []
    return infix(node.left) + [node.value] + infix(node.right)      # [node.value]: a LIST, not node.value


def postfix(node):
    if node is None:
        return []
    return postfix(node.left) + postfix(node.right) + [node.value]


def bfs(root):
    """Level by level, left to right. FIFO queue: pop from the left, push children on the right."""
    if root is None:
        return []
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        result.append(node.value)
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)
    return result


def levels(root):
    """[[level 0 values], [level 1 values], ...]"""
    result = []
    current = [root] if root is not None else []
    while current:
        result.append([n.value for n in current])
        current = [child for n in current for child in (n.left, n.right) if child is not None]
    return result


def leaves(node):
    """Values of the leaves, left to right."""
    if node is None:
        return []
    if node.left is None and node.right is None:
        return [node.value]
    return leaves(node.left) + leaves(node.right)


def all_paths(node):
    """Every root-to-leaf path as a list of values."""
    if node is None:
        return []
    if node.left is None and node.right is None:
        return [[node.value]]
    return [[node.value] + p for p in all_paths(node.left) + all_paths(node.right)]


def values_at_depth(node, d):
    if node is None:
        return []
    if d == 0:
        return [node.value]
    return values_at_depth(node.left, d - 1) + values_at_depth(node.right, d - 1)


# ---------------------------------------------------------------------------------------------
# 3. BINARY SEARCH TREE : left subtree < node < right subtree (at ALL depths)
#    find / min / max / insert : O(height) = O(log n) balanced, O(n) worst case
# ---------------------------------------------------------------------------------------------
def bst_find(node, value):
    if node is None:
        return False
    if value == node.value:
        return True
    if value < node.value:
        return bst_find(node.left, value)        # only ONE side: that is why it is fast
    return bst_find(node.right, value)


def bst_min(node):
    while node.left is not None:                 # smallest = go left as far as possible
        node = node.left
    return node.value


def bst_max(node):
    while node.right is not None:
        node = node.right
    return node.value


def bst_insert(node, value):
    """Returns the (new) root. Usage:  root = bst_insert(root, 5)   <- do not forget to reassign"""
    if node is None:
        return Node(value)
    if value < node.value:
        node.left = bst_insert(node.left, value)
    elif value > node.value:
        node.right = bst_insert(node.right, value)
    return node                                  # equal value: already there, nothing to do


def bst_from_list(values):
    root = None
    for v in values:
        root = bst_insert(root, v)
    return root


def bst_delete(node, value):
    """Returns the new root of the subtree. 3 cases: leaf, one child, two children."""
    if node is None:
        return None
    if value < node.value:
        node.left = bst_delete(node.left, value)
    elif value > node.value:
        node.right = bst_delete(node.right, value)
    else:
        if node.left is None:
            return node.right                    # 0 or 1 child: replace the node by its child
        if node.right is None:
            return node.left
        successor = bst_min(node.right)          # 2 children: copy the smallest of the right side...
        node.value = successor
        node.right = bst_delete(node.right, successor)   # ...then delete that one
    return node


def is_bst(node, low=None, high=None):
    """The interval (low, high) in which the values must be is PASSED DOWN: checking the direct
    children only is not enough (a deep value can break the order)."""
    if node is None:
        return True
    if low is not None and node.value <= low:
        return False
    if high is not None and node.value >= high:
        return False
    return is_bst(node.left, low, node.value) and is_bst(node.right, node.value, high)


def bst_floor(node, value):
    """Largest value <= `value` in a BST, or None."""
    if node is None:
        return None
    if node.value == value:
        return value
    if node.value > value:
        return bst_floor(node.left, value)
    better = bst_floor(node.right, value)
    return node.value if better is None else better


def sorted_list_to_bst(values):
    """Balanced BST from a SORTED list: the middle becomes the root (divide and conquer)."""
    if not values:
        return None
    middle = len(values) // 2
    return Node(values[middle], sorted_list_to_bst(values[:middle]), sorted_list_to_bst(values[middle + 1:]))


# ---------------------------------------------------------------------------------------------
# 4. A TREE AS A CLASS (methods instead of functions) + inheritance
# ---------------------------------------------------------------------------------------------
class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def height(self):
        return height(self.root)

    def infix(self):
        return infix(self.root)

    def __len__(self):
        return size(self.root)


class BinarySearchTree(BinaryTree):
    def __init__(self, values=()):
        super().__init__(None)                   # call the parent constructor
        for v in values:
            self.insert(v)

    def insert(self, value):
        self.root = bst_insert(self.root, value)

    def __contains__(self, value):               # makes `5 in tree` work
        return bst_find(self.root, value)


# ---------------------------------------------------------------------------------------------
# 5. EXPRESSION TREES (leaves = numbers, internal nodes = operators)
# ---------------------------------------------------------------------------------------------
def evaluate_expression(node):
    if node.left is None and node.right is None:
        return node.value
    a = evaluate_expression(node.left)
    b = evaluate_expression(node.right)
    if node.value == "+":
        return a + b
    if node.value == "-":
        return a - b
    if node.value == "*":
        return a * b
    return a / b


# ---------------------------------------------------------------------------------------------
if __name__ == "__main__":
    tree = Node(8,
                Node(3, Node(1), Node(6, Node(4), Node(7))),
                Node(10, None, Node(14, Node(13))))

    assert size(tree) == 9 and size(None) == 0
    assert height(tree) == 4 and height(None) == 0 and height(Node(1)) == 1
    assert count_leaves(tree) == 4 and count_leaves(None) == 0
    assert tree_sum(tree) == 66
    assert tree_max(tree) == 14 and tree_max(None) is None
    assert count_internal(tree) == 5
    assert count_equal(tree, 6) == 1
    assert contains(tree, 13) and not contains(tree, 5)
    assert depth_of(tree, 13) == 3 and depth_of(tree, 99) == -1
    assert not is_balanced(tree) and is_balanced(Node(1, Node(2), Node(3)))
    assert same_tree(tree, tree) and not same_tree(tree, mirror(tree))
    assert infix(mirror(tree)) == infix(tree)[::-1]

    assert prefix(tree) == [8, 3, 1, 6, 4, 7, 10, 14, 13]
    assert infix(tree) == [1, 3, 4, 6, 7, 8, 10, 13, 14]
    assert postfix(tree) == [1, 4, 7, 6, 3, 13, 14, 10, 8]
    assert bfs(tree) == [8, 3, 10, 1, 6, 14, 4, 7, 13]
    assert levels(tree) == [[8], [3, 10], [1, 6, 14], [4, 7, 13]]
    assert leaves(tree) == [1, 4, 7, 13]
    assert all_paths(tree)[0] == [8, 3, 1] and len(all_paths(tree)) == 4
    assert values_at_depth(tree, 2) == [1, 6, 14]

    assert bst_find(tree, 7) and not bst_find(tree, 5)
    assert bst_min(tree) == 1 and bst_max(tree) == 14
    root = bst_from_list([8, 3, 10, 1, 6, 14, 4, 7, 13])
    assert infix(root) == [1, 3, 4, 6, 7, 8, 10, 13, 14] and same_tree(root, tree)
    root = bst_delete(root, 3)                    # node with two children
    assert infix(root) == [1, 4, 6, 7, 8, 10, 13, 14]
    root = bst_delete(root, 14)                   # node with one child
    assert infix(root) == [1, 4, 6, 7, 8, 10, 13]
    assert is_bst(tree)
    assert not is_bst(Node(5, Node(3, None, Node(6)), Node(8)))   # 6 is in the left side of 5 -> not a BST
    assert bst_floor(tree, 5) == 4 and bst_floor(tree, 0) is None
    assert height(sorted_list_to_bst(list(range(1, 16)))) == 4

    t = BinarySearchTree([5, 2, 8, 1])
    assert 8 in t and 7 not in t and len(t) == 4 and t.infix() == [1, 2, 5, 8] and t.height() == 3

    expr = Node("*", Node("+", Node(2), Node(3)), Node(4))          # (2 + 3) * 4
    assert evaluate_expression(expr) == 20

    print("trees: all OK")
