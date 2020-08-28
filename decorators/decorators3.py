# dec. function with argument and without argument
def func(f):
    def wrapper(*args, **kwargs):
        print('Started')
        f(*args, **kwargs)
        print('Ended')
    return wrapper

@func
def func2(x):
    print(x)
# in upper we may add several arguments

@func
def func3():
    print('I am func3')

func2(5)
func3()

