import functools

def cache_decorator(func):
    cache = {}
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Create a key from the function arguments
        key = (args, tuple(sorted(kwargs.items())))
        if key in cache:
            print(f"Returning cached result for {key}")
            return cache[key]
        else:
            print(f"Calculating result for {key}")
            result = func(*args, **kwargs)
            cache[key] = result
            return result
    return wrapper

@cache_decorator
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(10))
print(fibonacci(10)) # This call will use the cache
# Output:
# Calculating result for ((0,), ())
# ... (intermediate calculations) ...
# Calculating result for ((1,), ())
# 55
# Returning cached result for ((10,), ())
# 55
