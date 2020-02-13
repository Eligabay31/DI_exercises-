import time

def decorator(func):
    def wrapper():
        print(f'running {func}')
        func()
        print('done')

    return wrapper

@decorator
def talk():
    print('some talk')



def timeit(func):
    def wrapper():
        start = time.perf_counter()
        func()
        end = time.perf_counter() - start
        print(f"function took: {end}")

    return wrapper

def computer():
    return 2**5

   if __name__ == '__main__':

       talk()



