from stock import Product


class Basket:
    def __init__(self, product, price):
        self.product = product
        self.price = price
        self.list_of_products = []

    def add_product_to_basket(self, product):
        self.list_of_products.append(product)


    def show_all_in_basket(self):
        for n, product in enumerate(self.list_of_products):
            print(f'{n + 1}: {product.name} - 1 шт.; цена: {product.price} руб.; (рейтинг товара:{product.rating})')


    def sum_price_all_in_basket(self):
        sum_ = 0
        for n, product in enumerate(self.list_of_products):
            sum_ = sum_ + product.price
        return sum_


    def print_all_in_basket(self):
        for n, product in enumerate(self.list_of_products):
            print(f'{n + 1}: {product.name} - 1 шт.; цена: {product.price} руб.')


def show_all_in_basket(self):
    for n, product in enumerate(self.list_of_products):
        print(f'{n + 1}: {product.name} - 1 шт.; цена: {product.price} руб.; (рейтинг товара:{product.rating})')
