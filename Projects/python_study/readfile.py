
def get_recipes(file_name: str):
    cook_book = {}
    with open(file_name, 'rt', encoding = 'utf-8') as file:
        for line in file:
            if '|' not in line and len(line) > 2:
                dish = line.split('\n')[0]
                cook_book[dish] = []
                quantity = int(file.readline())
                for ingr in range(quantity):
                    ingr = file.readline().split(' | ')
                    cook_book[dish].append({'ingredient_name': ingr[0],
                                            'quantity': int(ingr[1]),
                                           'measure': ingr[2].replace('\n', '')})
    return cook_book

print(get_recipes('recipes.txt'))

example_book = {
  'Омлет': [
    {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
    {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
    {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
    ],
  'Утка по-пекински': [
    {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
    {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
    {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
    {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
    ],
  'Запеченный картофель': [
    {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
    {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
    {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
    ]
  }