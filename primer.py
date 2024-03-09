from logger_2 import logger
from pprint import pprint


@logger('log_1.log')
def read_cook_book(recipes):
    with open(recipes, encoding='UTF-8') as file:
        cook_book = {}
        for line in file:
            dish_name = line.strip()
            ingredient_list = []
            for _ in range(int(file.readline())):
                ingredient = file.readline().strip().split(' | ')
                ingredient_list.append({'ingredient_name': ingredient[0],
                                        'quantity': int(ingredient[1]),
                                        'measure': ingredient[2]})
            file.readline()
            cook_book.update({dish_name: ingredient_list})
        return cook_book


@logger('log_2.log')
def get_shop_list_by_dishes(dishes, person_count):
    cook_book = read_cook_book('recipes.txt')
    shop_list = {}
    for dish in dishes:
        if dish in cook_book:
            for ing in cook_book[dish]:
                if ing['ingredient_name'] in shop_list:
                    shop_list[ing['ingredient_name']]['quantity'] += int(ing['quantity'] * person_count)
                else:
                    shop_list[ing['ingredient_name']] = {'measure': ing['measure'],
                                                         'quantity': (ing['quantity'] * person_count)}
        else:
            print(f'Блюда {dish} нет в книге рецептов')
    pprint(shop_list)


pprint(read_cook_book('recipes.txt'))
get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)