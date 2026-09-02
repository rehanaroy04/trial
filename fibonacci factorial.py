def fibonacci(n):
    """Generate Fibonacci series up to n terms"""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib

def factorial(n):
    """Calculate factorial of n"""
    if n < 0:
        return "Error: Factorial not defined for negative numbers"
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Example usage
print(fibonacci(10))    # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
print(factorial(5))     # 120