from src.trees import Node

#        8
#      /   \
#     3     10
#    / \      \
#   1   6      14
BST = Node(8, Node(3, Node(1), Node(6)), Node(10, None, Node(14)))

# NOT a BST: 12 is in the left subtree of 8 although 12 > 8
# (every parent-child pair looks correct locally)
NOT_BST = Node(8, Node(3, Node(1), Node(12)), Node(10))


def test_height():
    from src.trees import height

    assert height(None) == 0
    assert height(Node(1)) == 1
    assert height(BST) == 3
    chain = Node(1, Node(2, Node(3, Node(4))))
    assert height(chain) == 4


def test_count_leaves():
    from src.trees import count_leaves

    assert count_leaves(None) == 0
    assert count_leaves(Node(1)) == 1
    assert count_leaves(BST) == 3  # 1, 6, 14
    assert count_leaves(Node(1, Node(2))) == 1  # only one leaf: the node 2


def test_tree_sum():
    from src.trees import tree_sum

    assert tree_sum(None) == 0
    assert tree_sum(BST) == 8 + 3 + 10 + 1 + 6 + 14


def test_contains():
    from src.trees import contains

    assert contains(BST, 14) is True
    assert contains(BST, 1) is True
    assert contains(BST, 7) is False
    assert contains(None, 1) is False
    assert contains(NOT_BST, 12) is True  # it is in the tree, whatever the order


def test_collect_infix():
    from src.trees import collect_infix

    assert collect_infix(None) == []
    assert collect_infix(BST) == [1, 3, 6, 8, 10, 14]


def test_is_bst():
    from src.trees import is_bst

    assert is_bst(None) is True
    assert is_bst(Node(5)) is True
    assert is_bst(BST) is True
    assert is_bst(NOT_BST) is False
    assert is_bst(Node(5, Node(5))) is False  # duplicates are not allowed
