
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

def get_shop_list_by_dishes(dishes: list, person_count: int):
    cook_book = get_recipes('recipes.txt')
    shopping_list = {}
    for dish in dishes:
        if dish in cook_book.keys():
            for ingredient in cook_book[dish]:
                if ingredient['ingredient_name'] not in shopping_list.keys():
                    new_line = {ingredient['ingredient_name'] : {'measure':  ingredient['measure'],'quantity': int(ingredient['quantity'])*person_count}}
                    shopping_list.update(new_line)
                else:
                    item = ingredient["ingredient_name"]
                    shopping_list[item]["quantity"] += int(ingredient["quantity"])*person_count
    return shopping_list

print(get_shop_list_by_dishes(['Омлет', 'Фахитос'], 4))
