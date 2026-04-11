def calculate_discount(price, discount_rate, user_tier):
    """Return the price after applying a tier-adjusted discount rate."""
    tier_bonus = {
        "bronze": 0.00,
        "silver": 0.02,
        "gold": 0.05,
        "platinum": 0.08,
    }
    effective_rate = discount_rate + tier_bonus.get(user_tier.lower(), 0.00)
    return price * (1 - effective_rate)
