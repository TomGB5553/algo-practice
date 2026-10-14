"""Helpers used by the tests to look at the REAL code of a function (comments and docstrings are ignored)."""
import ast
import inspect
import textwrap


def _tree(func):
    return ast.parse(textwrap.dedent(inspect.getsource(func)))


def called_names(func):
    """Names of everything called inside func: f(...) gives 'f', obj.m(...) gives 'm'."""
    names = []
    for node in ast.walk(_tree(func)):
        if isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name):
                names.append(node.func.id)
            elif isinstance(node.func, ast.Attribute):
                names.append(node.func.attr)
    return names


def uses_power_operator(func):
    return any(isinstance(n, ast.BinOp) and isinstance(n.op, ast.Pow) for n in ast.walk(_tree(func)))
