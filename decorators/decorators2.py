# dec. function with argument
def func(f):
    def wrapper(x):
        print('Started')
        f(x)
        print('Ended')
    return wrapper

@func
def func2(x):
    print(x)

@func
def func3():
    print('I am func3')

func2(5)

# if we run below func we get error
# wrapper wait argument
# solution on decorators3.py file
# func3()

