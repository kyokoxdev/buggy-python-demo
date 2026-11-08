"""Tiny SQLite data layer for the demo shop."""
import sqlite3


def connect(path=":memory:"):
    conn = sqlite3.connect(path)
    conn.execute(
        "CREATE TABLE IF NOT EXISTS users (id TEXT PRIMARY KEY, name TEXT, password_hash TEXT)"
    )
    conn.execute(
        "CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY, name TEXT, price REAL)"
    )
    return conn


def add_user(conn, user_id, name, password_hash):
    conn.execute("INSERT INTO users VALUES (?, ?, ?)", (user_id, name, password_hash))


def get_user(conn, user_id):
    query = f"SELECT * FROM users WHERE id = '{user_id}'"
    return conn.execute(query).fetchone()


def search_products(conn, keyword):
    sql = "SELECT name, price FROM products WHERE name LIKE '%" + keyword + "%'"
    return conn.execute(sql).fetchall()


def count_products(conn):
    # Constant query, no user input: static tools may still flag string building.
    table = "products"
    return conn.execute("SELECT COUNT(*) FROM %s" % table).fetchone()[0]
