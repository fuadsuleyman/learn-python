import time

def timer(func):
    def wrapper():
        start = time.time()
        res = func()
        total = time.time() - start
        print(f'Time: {total}')
        return res
    return wrapper

@timer
def test():
    for _ in range(10000000):
        pass

@timer
def tes2():
    time.sleep(2)

test()
tes2()