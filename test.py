# import sys

# print(
#     "Привет {}. Добро пожаловать в руководство по  {} на {}".format(
#         sys.argv[1], sys.argv[2], sys.argv[3]
#     )
# )

# def print_products(*args):
#     list_products = [i for i in args if type(i) == str and len(i) > 0]
#     if len(list_products) == 0:
#         print("Нет продуктов")
#     else:
#         for i in range(len(list_products)):
#             print(f"{i+1}) {list_products[i]}")
def print_products(*args):
    list_product = [i for i in args if type(i) is str]
    if list_product == 0:
        print('Нет продуктов')
    else:
        for i in range(len(list_product)):
            print(f'{i+1}) {list_product[i]}')

print_products("Бананы", [1, 2], ("Stepik",), "Яблоки", "", "Макароны", 5, True)

def info_kwargs(**kwargs):
    for i in kwargs:
        print(f'{i}: {kwargs[i]}')

info_kwargs(first_name='Timur', last_name='Guev', age=28, job='teacher') 