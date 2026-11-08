import pytest

from shop.security import check_password, hash_password, make_reset_token, require_admin
from shop.tools import calculate


def test_password_roundtrip():
    assert check_password("hunter2", hash_password("hunter2"))
    assert not check_password("wrong", hash_password("hunter2"))


def test_reset_token_length():
    assert len(make_reset_token()) == 32


def test_require_admin_rejects_non_admin():
    with pytest.raises(PermissionError):
        require_admin({"role": "user"})


def test_calculate():
    assert calculate("2 + 3 * 4") == 14
    assert calculate("(1 + 1) / 4") == 0.5


def test_calculate_rejects_code():
    with pytest.raises(ValueError):
        calculate("__import__('os').system('echo pwned')")
