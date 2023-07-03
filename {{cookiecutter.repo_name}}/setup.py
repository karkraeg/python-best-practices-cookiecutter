import setuptools

"""
Is needed to install the package locally via `pip install -e .`
"""


setuptools.setup(
    name="{{cookiecutter.repo_name}}",
    packages=setuptools.find_packages(),
)
