from decimal import Decimal
from typing import List


# Find the bug
def calculate_total_price(prices: List[Decimal], discount_threshold: Decimal, discount_rate: Decimal) -> Decimal:
    total = sum(prices, Decimal(0))
    one  = Decimal(1)
    if total > discount_threshold:
        total *= (one - discount_rate)
    return total
