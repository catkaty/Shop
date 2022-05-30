from stock import Product


class Basket:
    def __init__(self, product, count):
        self.product = product
        self.count = count
        self.__products = []

    def add_to_basket(self, product: Product):
        self.__products.append(product)
        print("{0} добавлен".format(Product))
