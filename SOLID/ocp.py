class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item.price
        return total

#add discount functionality
class ShoppingCartWithDiscount(ShoppingCart):
    def apply_discount(self):
        total = super().calculate_total()
        # Apply a discount logic here
        return total * 0.9  # 10% discount

# Example usage:
cart = ShoppingCartWithDiscount()
cart.add_item(Product("Item 1", 20))
cart.add_item(Product("Item 2", 30))
cart.apply_discount()
