
def hello_f(name, age):
    try: #создаем исключение
        if not type(name) is str: #если name не строка
            raise ValueError("Имя должно содержать  только строчные и заглавные буквы.") #не может быть выполнена с переменной не этого(str) типа
        if not type(age) is int: #если name не строка
            raise ValueError("Возраст должен содержать только цифры!") #если age не число
    except ValueError as e: #оператор as собирает информацию об исключении передаёт в переменную e
        print(e)
        return #завершаем функцию, возвращаем ее значения к выводу

    print(f'Привет, {name}')
    print(f'Тебе, {age}, лет')

hello_f("John", 30) #Верный вывод
hello_f(30, 30) #допущена ошибка