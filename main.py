from stock import Categories, Product
from user import check_password
from user import User

def run(self):
    print('Магазин продуктов')

    login = input('Введите логин: ')
    password = input('Введите пароль: ')
        # login = 'Olga'
        # password = '12345'
    if not check_password(login, password):
        print('Вы не зарегестрированы')
        ans = True
        while ans:
            print('Выберите категорию: ')
            self.show_all_categories()
            while True:
                try:
                    print('Выберите продукт: ')
                except





