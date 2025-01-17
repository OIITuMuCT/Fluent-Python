# def print_products(*args):

#     a = [args[i] for i in range(len(args)) if isinstance(args[i], 1)]

#     for i in range(len(a)):
#         print(f'{i+1}) {a[i]}')


# print_products("Бананы", [1, 2], ("Stepik",), "Яблоки", "", "Макароны", 5, True)
def info_kwargs(**kwargs):
    for key, value in sorted(kwargs.items()):
        print(f"{key}: {value}")


info_kwargs(first_name="Timur", last_name="Guev", age=28, job="teacher", mobile="920343453872")
