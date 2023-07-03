from {{cookiecutter.repo_name}}.{{cookiecutter.repo_name}} import calc_sum


def test_calc_sum() -> None:
    assert calc_sum(5,5) == 10
