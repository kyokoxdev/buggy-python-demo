from shop.cart import (add_item, apply_discount, average_price, cart_total,
                       is_free_shipping, paginate, parse_quantity)


def test_add_item_fresh_cart_each_call():
    assert add_item("apple") == ["apple"]
    assert add_item("pear") == ["pear"]


def test_cart_total():
    assert cart_total([10, 20, 30]) == 60


def test_apply_discount():
    assert apply_discount(200, 10) == 180


def test_average_price_empty():
    assert average_price([]) == 0


def test_average_price():
    assert average_price([2, 4]) == 3


def test_paginate_first_page():
    assert paginate(list(range(25)), 1) == list(range(10))


def test_parse_quantity():
    assert parse_quantity("3") == 3
    assert parse_quantity("x") == 0


def test_free_shipping():
    assert is_free_shipping(60, None)
    assert is_free_shipping(10, True)
    assert not is_free_shipping(10, None)
