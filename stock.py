class Categories:
    def __init__(self, name_cat: str, list_of_products):
        self.name_cat = name_cat
        self.list_of_products = list_of_products

    def add_to_categories(self, product):
        self.list_of_products.append(product)

    def add_all_to_categories(self, products):
        for product in products:
            self.add_to_categories(product)

    def show_all_categories(self):
        print(Categories)


class Product:

    def __init__(self, name: str, price: int, rating):
        self.id = 0
        self.name = name
        self.price = price
        self.rating = rating
