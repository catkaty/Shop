from stock import Categories, Product

category_1 = Categories('Фрукты', [Product('Яблоки', 100, 1),
                                   Product('Персики', 200, 2),
                                   Product('Апельсины', 90, 3),
                                   Product('Бананы', 80, 4),
                                   Product('Груши', 200, 5),
                                   Product('Абрикосы', 300, 5),
                                   Product('Лимоны', 250, 3)])
category_2 = Categories('Овощи', [Product('Томаты', 200, 3),
                                  Product('Огурцы', 120, 3),
                                  Product('Картофель', 60, 4),
                                  Product('Перец', 350, 5),
                                  Product('Морковь', 40, 5),
                                  Product('Лук', 40, 2),
                                  Product('Цукини', 220, 5)])
category_3 = Categories('Мясо', [Product('Свинина', 400, 2),
                                 Product('Говядина', 600, 1),
                                 Product('Баранина', 600, 1),
                                 Product('Крольчатина', 450, 1),
                                 Product('Оленина', 900, 5),
                                 Product('Медвежатина', 1000, 3),
                                 Product('Индюшатина', 400, 3)])

CAT = [category_1, category_2, category_3]
