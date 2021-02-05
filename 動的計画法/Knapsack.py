class Item:
    def __init__(self, w = 0, p = 0):
            self.weight = w
            self.price = p

items = [ Item(300, 400), Item(500, 250), Item(200, 980), \
          Item(600, 340), Item(900, 670), Item(1360, 780), \
          Item(800, 570), Item(250, 800)]

def Knapsack(i, w):
    if i >= len(items):
        return 0
    elif w - items[i].weight < 0.0:
        return Knapsack(i+1, w)
    else:
        p1 = Knapsack(i + 1, w)
        p2 = Knapsack(i + 1, w - items[i].weight) + items[i].price
        if p1 > p2:
            return p1
        else:
            return p2

p = Knapsack(0, 2500)
print(f"TOTAL PRICE = {p}")