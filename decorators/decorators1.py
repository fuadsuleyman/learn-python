def func(f):
    def wrapper():
        print('Started')
        f()
        print('Ended')
    return wrapper

@func
def func2():
    print('I am func2')

# this dec. it is same as func2 = func(func2)
@func
def func3():
    print('I am func3')

# func2 and func3 here is new variables
# func2 = func(func2) 
# func3 = func(func3)

func2()
func3()

