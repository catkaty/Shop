import basket
from user import check_password
from user import User
from category_cat import CAT
import random


class Shop:
    def __init__(self, category):
        self.basket = basket
        self.category = category

    def start(self):
        global current_cat
        print('Магазин продуктов')

        login = input('Введите логин: ')
        password = input('Введите пароль: ')
        # login = 'Olga'
        # password = '12345'
        if not check_password(login, password):
            print('Вы не зарегистрированы')
            return
        self.user = User(login, password)
        ans = True
        while ans:
            print('Выберите категорию: ')
            self.show_all_categories()
            while True:
                try:
                    current_cat = int(input('Выберите категорию : ')) - 1
                    if current_cat > len(self.category) - 1 or current_cat < 0:
                        raise ValueError
                    break
                except ValueError:
                    print('Ошибка!')
                    print(f"Введите целое число от 1 до {len(self.category)}")
            self.show_categories_by_ID(current_cat)
            while True:
                try:
                    current_product = int(input('Выберите номер товара: ')) - 1
                    if current_product > len(self.category[current_cat].list_of_products) - 1 or current_product < 0:
                        raise ValueError
                    break
                except ValueError:
                    print('Ошибка!')
                    print(f"Введите целое число от 1 до {len(self.category[current_cat].list_of_products)}")
            self.add_product_to_basket(current_cat, current_product)
            print('Товары в корзине:')
            self.show_all_in_basket()
            print(
                'Продолжить покупки- введите Y(y);'
                ' Завершить покупки- введите любой другой символ:')
            if input().lower() == 'y':
                ans = True
            else:
                ans = False
        summa = self.sum_price_all_in_basket()
        ch = random.randrange(1000, 9999, 1)
        print("Товары:")
        self.print_all_in_basket()
        print(f"Итог: {summa} руб.")

    def show_all_categories(self):
        for n, categories in enumerate(self.category):
            print(f'{n + 1}: {categories.name_cat}')

    def show_categories_by_ID(self, categories_ID):
        print(f'Выбранная для просмотра категория: {self.category[categories_ID].name_cat}')
        for n, product in enumerate(self.category[categories_ID].list_of_products):
            print(f'{n + 1}: {product.name}; цена за 1 шт.: {product.price} руб.; (рейтинг товара:{product.rating})')

    def show_category_by_ID(self, current_cat):
        pass

    def sum_price_all_in_basket(self):
        pass

    def print_all_in_basket(self):
        pass

    def add_product_to_basket(self, current_cat, current_product):
        pass



if __name__ == '__main__':
    mag = Shop(CAT)
    mag.start()
