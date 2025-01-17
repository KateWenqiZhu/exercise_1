from polynomials import Polynomial
import pytest

def test_print():

    p = Polynomial((2, 1, 0, 3))

    assert str(p) == "3x^3 + x + 2"

    f = Polynomial((1, 1, 0, 4, 5))
    
    assert str(f) == "5x^4 + 4x^3 + x + 1"

    f1 = Polynomial((0, 0, 0))
    
    assert str(f1) == "0"



def test_equality():
    assert Polynomial((0, 1)) == Polynomial((0, 1))


@pytest.mark.parametrize(
    "a, b, sum",
    (((0,), (0, 1), (0, 1)),
     ((2, 0, 3), (1, 2), (3, 2, 3)),
     ((4, 2), (10, 2, 4), (14, 4, 4)))
    )
def test_add(a, b, sum):
    assert Polynomial(a) + Polynomial(b) == Polynomial(sum)


def test_add_scalar():
    assert Polynomial((2, 1)) + 3 == Polynomial((5, 1))


def test_reverse_add_scalar():
    assert 3 + Polynomial((2, 1)) == Polynomial((5, 1))


def test_add_unknown():
    with pytest.raises(TypeError):
        Polynomial((1,)) + "frog"