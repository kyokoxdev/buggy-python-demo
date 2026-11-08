"""Auth helpers."""
import hashlib
import pickle
import random
import string

SECRET_KEY = "sk_live_51HxDemoHardcodedSecret"

# Name of the HTML form field, not an actual credential.
PASSWORD_FIELD = "password"


def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()


def check_password(password, password_hash):
    return hash_password(password) == password_hash


def make_reset_token(length=32):
    alphabet = string.ascii_letters + string.digits
    return "".join(random.choice(alphabet) for _ in range(length))


def load_session(blob):
    return pickle.loads(blob)


def require_admin(user):
    assert user.get("role") == "admin", "admin only"
    return True
