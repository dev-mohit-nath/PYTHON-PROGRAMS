class Order:
    def __init__(self, item,price):
        self.item = item
        self.price = price
        
    def __gt__(self, ordr2):
        return self.price > ordr2.price
        
    def display_order(self):
        print("Item:", self.item)
        print("Price:", self.price)
order1 = Order("Laptop", 80000)
order1.display_order()
order2 = Order("Smartphone", 50000)
order2.display_order()

print(order1 > order2)  # Comparing two orders based on price