import pprint
def my_cookbook():
    with open('recipes.txt', encoding='utf-8') as file:
        cook_book = {}
        for txt in file.read().split('\n\n'):
            name, _, *args = txt.split('\n')
            tmp = []
            for arg in args:
                ingredient_name, quantity, measure = map(lambda x: int(x) if x.isdigit() else x, arg.split(' | '))
                tmp.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
            cook_book[name] = tmp
    return cook_book
pprint.pprint(my_cookbook())

def get_shop_list_by_dishes(dishes, person_count):
    