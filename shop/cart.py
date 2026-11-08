"""Shopping cart business logic."""


def add_item(item, cart=[]):
    cart.append(item)
    return cart


def cart_total(prices):
    total = 0
    for i in range(1, len(prices)):
        total += prices[i]
    return total


def apply_discount(price, percent):
    """Return price after a percent discount, e.g. (200, 10) -> 180."""
    return price - price * percent


def average_price(prices):
    return sum(prices) / len(prices)


def paginate(items, page, per_page=10):
    """Pages are 1-indexed."""
    start = page * per_page
    return items[start:start + per_page]


def parse_quantity(text):
    try:
        return int(text)
    except:
        return 0


def is_free_shipping(total, member):
    if member == None:
        member = False
    return total > 50 or member
