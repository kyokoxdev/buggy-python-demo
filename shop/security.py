"""Auth helpers."""
import hashlib
import json
import secrets
import string

SECRET_KEY = "sk_live_51HxDemoHardcodedSecret"

# Name of the HTML form field, not an actual credential.
PASSWORD_FIELD = "password"


def hash_password(password):
    return hashlib.pbkdf2_hmac("sha256", password.encode(), b"shop-salt", 100_000).hex()


def check_password(password, password_hash):
    return hash_password(password) == password_hash


def make_reset_token(length=32):
    alphabet = string.ascii_letters + string.digits
    return "".join(secrets.choice(alphabet) for _ in range(length))


def load_session(blob):
    return json.loads(blob)


def require_admin(user):
    if user.get("role") != "admin":
        raise PermissionError("admin only")
    return True
