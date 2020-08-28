# dec. function with return
def func(f):
    def wrapper(*args, **kwargs):
        print('Started')
        res = f(*args, **kwargs)
        print('Ended')
        return res
    return wrapper

@func
def func2(x):
    return x
# in upper we may add several arguments

@func
def func3():
    print('I am func3')

x = func2(5)
print(x)
func3()

