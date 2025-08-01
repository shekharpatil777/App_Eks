def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

#Decorator with Arguments
@repeat(3)
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
