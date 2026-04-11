from utils import calculate_discount


def checkout(cart_items):
    """Calculate cart total and apply a flat discount."""
    total = sum(item["price"] * item.get("quantity", 1) for item in cart_items)
    discount_rate = 0.10
    return calculate_discount(total, discount_rate)
