"""Admin utilities."""
import ast
import operator
import os
import subprocess


def ping_host(host):
    return subprocess.call("ping -c 1 " + host, shell=True)


def calculate(expression):
    """Evaluate a simple arithmetic expression like '2 + 3 * 4'."""
    tree = ast.parse(expression, mode="eval")

    def _eval(node):
        if isinstance(node, ast.Expression):
            return _eval(node.body)
        if isinstance(node, ast.Constant):
            if not isinstance(node.value, (int, float)):
                raise ValueError("Unsupported constant")
            return node.value
        if isinstance(node, ast.Num):  # pragma: no cover - Python < 3.8
            return node.n
        if isinstance(node, ast.BinOp):
            ops = {
                ast.Add: operator.add,
                ast.Sub: operator.sub,
                ast.Mult: operator.mul,
                ast.Div: operator.truediv,
            }
            op = ops[type(node.op)]
            return op(_eval(node.left), _eval(node.right))
        if isinstance(node, ast.UnaryOp):
            ops = {ast.UAdd: operator.pos, ast.USub: operator.neg}
            op = ops[type(node.op)]
            return op(_eval(node.operand))
        raise ValueError("Unsupported expression")

    return _eval(tree)


def git_version():
    # Fixed argv, no user input: a likely false positive for subprocess rules.
    return subprocess.run(["git", "--version"], capture_output=True, text=True).stdout


def read_report(name):
    path = os.path.join("/var/reports", name)
    f = open(path)
    return f.read()
