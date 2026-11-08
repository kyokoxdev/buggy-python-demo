from shop.db import add_user, connect, count_products, get_user, search_products


def make_db():
    conn = connect()
    add_user(conn, "u1", "Alice", "h1")
    conn.execute("INSERT INTO products (name, price) VALUES ('Red Apple', 1.5), ('Pear', 2.0)")
    return conn


def test_get_user():
    assert get_user(make_db(), "u1")[1] == "Alice"


def test_get_user_injection_returns_nothing():
    assert get_user(make_db(), "x' OR '1'='1") is None


def test_search_products():
    assert search_products(make_db(), "Apple") == [("Red Apple", 1.5)]


def test_count_products():
    assert count_products(make_db()) == 2
