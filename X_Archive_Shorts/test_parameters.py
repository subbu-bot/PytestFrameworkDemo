import pytest


@pytest.mark.parametrize("num, result", [(2, 22), (3, 33), (5, 55), (4, 90)])
def test_paramdiv(num, result):
    assert 11 * num == result

