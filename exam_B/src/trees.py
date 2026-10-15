class Node:
    """A node of a binary tree. A missing child is None."""

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# Exercise 4 : write your functions here

def height(node):
    if node==None:
        return 0
    return 1+max(height(node.left), height(node.right))

def count_leaves(node):
    if node is None:
        return 0
    if node.left is None and node.right is None:
        return 1
    return count_leaves(node.left) + count_leaves(node.right)

def tree_sum(node):
    if node is None:                ## is None !! et PAS =None XXXXX
        return 0
    return node.value + tree_sum(node.left) + tree_sum(node.right)

def contains(node, value):
    if node is None:
        return False
    return node.value == value or contains(node.left, value) or contains(node.right, value)

def collect_infix(node):
    out=[]
    if node is None:
        return []
    out.append(collect_infix(node.left))
    out.append(collect_infix(node.value))
    out.append(collect_infix(node.right))
    return out
    
    




    