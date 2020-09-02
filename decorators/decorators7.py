def kvarrat_decorator(func):
    def wrapper():
        funcResult=func()
        newResult=funcResult**2
        return newResult
    return wrapper

@kvarrat_decorator
def someFunc():
    data=int(input('Eded daxile et: '))
    return data/2

print(someFunc())
