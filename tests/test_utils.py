import pytest
from src.utils import apply_discount, is_strong_password


def test_apply_discount_normal():
    assert apply_discount(100, 10) == 90.0
    assert apply_discount(50, 0) == 50.0


def test_apply_discount_edge_cases():
    assert apply_discount(0, 50) == 0.0
    assert apply_discount(100, 100) == 0.0


def test_apply_discount_invalid_price():
    with pytest.raises(ValueError):
        apply_discount(-1, 10)


def test_apply_discount_invalid_discount():
    with pytest.raises(ValueError):
        apply_discount(100, -5)
    with pytest.raises(ValueError):
        apply_discount(100, 120)


def test_is_strong_password_valid():
    assert is_strong_password("Aa123456")
    assert is_strong_password("GoodPass1")


def test_is_strong_password_invalid():
    assert not is_strong_password("short1")
    assert not is_strong_password("alllowercase1")
    assert not is_strong_password("ALLUPPERCASE1")
    assert not is_strong_password("NoDigitsHere")
