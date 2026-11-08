g = (x*6 for x in [1,2,3])
print(list(g))


def announce(func):
    def wrapper():
        print("Сейчас вызов")
        result = func()
        print('Готово')
        return result
    return wrapper

@announce
def hello():
    print("Привет!")

hello()
