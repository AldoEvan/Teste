from calc import somar
from calc import subtrair
from calc import mult
from calc import div


def test_somar():
    assert somar(4, 4) == 8


def test_subtrair():
    assert subtrair(4, 4) == 0


def test_mult():
    assert mult(4,4) == 16


def test_div():
    assert div(4,4) == 1
