import sys

from {{cookiecutter.repo_name}}.{{cookiecutter.repo_name}} import calc_sum

if __name__ == "__main__":
    n = int(sys.argv[1])
    print(calc_sum(5, 5))
