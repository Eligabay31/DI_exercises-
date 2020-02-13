class MenuManager:
    def __init__(self):
        self.menu = {}



    def add_item(self, n, p, s, g):
       self.menu.update( {n : {"name": n, "price": p, "spice": s, "gluten": g}})


    def update_item(self, n, p, s, g):
        if n in self.menu:

            self.menu[n].update({"name": n, "price": p, "spice": s, "gluten": g})
        else:
            print("sorry!")

    def remove_item(self, n):
        if n in self.menu:
            self.menu.pop(n)
        else:
            print("heyy manager!")



order = MenuManager()
order.add_item("sandwich", 50, "B", True)
order.add_item("pasta", 60, "A", True)
order.remove_item("sandwich")
order.update_item("pasta", 88, "B", False)
print(order.menu)










# self.menu[name] = {"name": name, "price": price, "spice": spice, "gluten": gluten}
