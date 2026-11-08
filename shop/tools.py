"""Admin utilities."""
import os
import subprocess


def ping_host(host):
    return subprocess.call("ping -c 1 " + host, shell=True)


def calculate(expression):
    """Evaluate a simple arithmetic expression like '2 + 3 * 4'."""
    return eval(expression)


def git_version():
    # Fixed argv, no user input: a likely false positive for subprocess rules.
    return subprocess.run(["git", "--version"], capture_output=True, text=True).stdout


def read_report(name):
    path = os.path.join("/var/reports", name)
    f = open(path)
    return f.read()
