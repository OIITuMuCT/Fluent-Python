def print_products(*args):

    a = [args[i] for i in range(len(args)) if isinstance(args[i], 1)]
    
    for i in range(len(a)):
        print(f'{i+1}) {a[i]}')


print_products("Бананы", [1, 2], ("Stepik",), "Яблоки", "", "Макароны", 5, True)
