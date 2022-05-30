users_list = {
    'Olga': '12345',
    'Anna': '67890'
}


class User:
    def __init__(self, login: str, password: str):
        self.login = login
        self.password = password


if __name__ == '__main__':
    user1 = User('Olga', '12345')
    user2 = User('Anna', '67890')


def check_password(login, password):
    try:
        if login in users_list and password in users_list and login == password:
            print(f'Здравствуйте {login}.')
            return True
        print('Пароль введен не верно.')
        return False
    except KeyError:
        print('Вы не зарегистрированы. Авторизуйтесь')
        return False


