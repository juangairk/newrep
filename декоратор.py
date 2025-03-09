# Декоратор
def my_decorator(func):
    def wrapper():
        print(f"Функция {func.__name__} начинает работу.")
        func()
        print(f"Функция {func.__name__} завершила работу.\n")
    return wrapper

# Функции с декоратором
@my_decorator
def say_hello():
    print("Привет!")

@my_decorator
def say_bye():
    print("Пока!")

@my_decorator
def say_name():
    print("Меня зовут Python!")

# Вызов функций
say_hello()
say_bye()
say_name()