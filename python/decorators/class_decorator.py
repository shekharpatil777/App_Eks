class MyClassDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print(f"Class decorator is calling '{self.func.__name__}'")
        return self.func(*args, **kwargs)

@MyClassDecorator
def multiply(a, b):
    return a * b

#A class can also be used as a decorator. The class must implement the __call__ method
print(multiply(4, 5))
# Output:
# Class decorator is calling 'multiply'
# 20
