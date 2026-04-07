def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Start")
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def add(a, b):
    print(a + b)

add(2, 3)