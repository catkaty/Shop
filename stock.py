
class Categories:
    def __init__(self, name: str, products=None):
        self.id_ = 0
        self.products = products
        self.name = name
        self.__products = []

    def add_to_categories(self, product):
        self.__products.append(product)

    def add_all_to_categories(self, products):
        for product in products:
            self.add_to_categories(product)

    def show_all_categories(self):
        print(Categories)


if __name__ == '__main__':
    category1 = Categories('Фрукты')
    print(category1)
    category2 = Categories('Овощи')
    print(category2)
    category3 = Categories('Мясо')
    print(category3)


class Product:

    def __init__(self, name: str, price: int, rating):
        self.name = name
        self.price = price
        self.rating = rating


if __name__ == '__main__':
    product1 = Product('Яблоки', 100, 1)
    print(product1)
    product2 = Product('Персики', 200, 2)
    print(product2)
    product3 = Product('Апельсины', 90, 3)
    print(product3)
    product4 = Product('Бананы', 80, 4)
    print(product4)
    product5 = Product('Груши', 200, 5)
    print(product5)
    product6 = Product('Томаты', 200, 6)
    print(product6)
    product7 = Product('Огурцы', 120, 7)
    print(product7)
    product8 = Product('Картофель', 60, 8)
    print(product8)
    product9 = Product('Перец', 350, 9)
    print(product9)
    product10 = Product('Морковь', 40, 10)
    print(product10)
    product11 = Product('Свинина', 400, 11)
    print(product11)
    product12 = Product('Говядина', 600, 12)
    print(product12)
    product13 = Product('Баранина', 600, 13)
    print(product13)
    product14 = Product('Крольчатина', 450, 14)
    print(product14)
    product15 = Product('Оленина', 700, 15)
    print(product15)



