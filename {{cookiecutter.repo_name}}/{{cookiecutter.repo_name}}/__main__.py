import sys
import click
from {{cookiecutter.repo_name}}.{{cookiecutter.repo_name}} import calc_sum

"""
The __main__.py file in Python serves as the entry point for running a package as a script. 
When you execute a Python package with the -m flag or by running the package directory itself,
Python looks for the __main__.py file and executes its contents.
"""


@click.command()
@click.option("--n", default=1)
def hello(n):
    """This is a summary."""
    print(calc_sum(n, 5))


if __name__ == "__main__":
    hello()
