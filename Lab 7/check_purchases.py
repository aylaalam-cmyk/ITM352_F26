def check_purchases(purchases, budget):
    total_spent = 0

    for purchase in purchases:
        total_spent += purchase
        if total_spent > budget:
            return f"This purchase {purchase} exceeds the budget!"

    return "All purchases are within the budget."


# Test cases
assert check_purchases([36.13, 23.87], 60) == "All purchases are within the budget."
assert check_purchases([36.13, 23.87, 183.35], 60) == "This purchase 183.35 exceeds the budget!"
assert check_purchases([10, 20, 15], 50) == "All purchases are within the budget."
assert check_purchases([20, 30, 20], 50) == "This purchase 20 exceeds the budget!"

# Example usage
recent_purchases = [36.13, 23.87, 183.35, 22.93, 11.62]
budget = 60
print(check_purchases(recent_purchases, budget))
