def my_decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

#Basic Function Decorator

@my_decorator
def greet():
    print("Hello!")

greet()
