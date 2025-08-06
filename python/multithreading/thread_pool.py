from concurrent.futures import ThreadPoolExecutor

#ThreadPoolExecutor (Modern Way with concurrent.futures
def square(n):
    return n * n

with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(square, [1, 2, 3, 4, 5])

print(list(results))
