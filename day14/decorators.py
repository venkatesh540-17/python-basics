def logging(func):
    def wrapper():
        print("starting")
        func()
        print("ending")
    return wrapper()

@logging
def add():
    print(2+1)
add()