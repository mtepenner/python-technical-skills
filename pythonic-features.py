# --- Comprehensions ---
# Creating a new list/dict/set efficiently in one line
squares = [x**2 for x in range(5)]
even_squares = {x: x**2 for x in range(5) if x % 2 == 0}

# --- Generators (Memory Efficiency) ---
# Yields items one at a time instead of storing them all in memory
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Using the generator
for num in fibonacci(5):
    print(num) # Outputs: 0, 1, 1, 2, 3

# --- Decorators ---
# Modifying the behavior of a function without changing its code
import time

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"Executed in {time.time() - start} seconds")
        return result
    return wrapper

@timer_decorator
def slow_function():
    time.sleep(1)

# --- Lambdas and Higher-Order Functions ---
# Small, anonymous functions for quick operations
nums = [1, 2, 3, 4]
doubled = list(map(lambda x: x * 2, nums))
evens = list(filter(lambda x: x % 2 == 0, nums))

# --- Context Managers ---
# Ensures resources are cleaned up (like closing a file automatically)
with open("test.txt", "w") as file:
    file.write("Hello, World!") 
# File is automatically closed here, even if an error occurs inside the block
