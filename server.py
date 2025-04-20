# server.py
from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("Demo")


# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

@mcp.tool()
def subtract(a: int, b: int) -> int:
    """minus two numbers"""
    return a - b


@mcp.tool()
def multiply(a: int, b: int) -> int:
    """multiply two numbers"""
    return a * b


@mcp.tool()
def divide(a: int, b: int) -> int:
    """divide two numbers"""
    try:
        return a / b
    except ZeroDivisionError:
        raise ZeroDivisionError("Division by zero is not allowed.")

@mcp.tool()
def power(a: int, b: int) -> int:
    """raise a number to the power of another"""
    return a ** b

@mcp.tool()
def factorial(n: int) -> int:
    """calculate the factorial of a number"""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

@mcp.tool()
def fibonacci(n: int) -> int:
    """calculate the nth Fibonacci number"""
    if n < 0:
        raise ValueError("Fibonacci is not defined for negative numbers.")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

@mcp.tool()
def prime(n: int) -> bool:
    """check if a number is prime"""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

@mcp.tool()
def gcd(a: int, b: int) -> int:
    """calculate the greatest common divisor of two numbers"""
    while b:
        a, b = b, a % b
    return a

@mcp.tool()
def lcm(a: int, b: int) -> int:
    """calculate the least common multiple of two numbers"""
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b)

@mcp.tool()
def is_even(n: int) -> bool:
    """check if a number is even"""
    return n % 2 == 0

@mcp.tool()
def is_odd(n: int) -> bool:
    """check if a number is odd"""
    return n % 2 != 0

@mcp.tool()
def square(n: int) -> int:
    """calculate the square of a number"""
    return n * n

@mcp.tool()
def cube(n: int) -> int:
    """calculate the cube of a number"""
    return n * n * n

@mcp.tool()
def sqrt(n: int) -> float:
    """calculate the square root of a number"""
    if n < 0:
        raise ValueError("Square root is not defined for negative numbers.")
    return n ** 0.5

@mcp.tool()
def log(n: int, base: int) -> float:
    """calculate the logarithm of a number with a given base"""
    if n <= 0:
        raise ValueError("Logarithm is not defined for non-positive numbers.")
    if base <= 1:
        raise ValueError("Base must be greater than 1.")
    return math.log(n, base)

@mcp.tool()
def sin(x: float) -> float:
    """calculate the sine of an angle in radians"""
    return math.sin(x)

@mcp.tool()
def cos(x: float) -> float:
    """calculate the cosine of an angle in radians"""
    return math.cos(x)

@mcp.tool()
def tan(x: float) -> float:
    """calculate the tangent of an angle in radians"""
    return math.tan(x)

@mcp.tool()
def asin(x: float) -> float:
    """calculate the arcsine of a value"""
    if x < -1 or x > 1:
        raise ValueError("Input must be in the range [-1, 1].")
    return math.asin(x)

@mcp.tool()
def acos(x: float) -> float:
    """calculate the arccosine of a value"""
    if x < -1 or x > 1:
        raise ValueError("Input must be in the range [-1, 1].")
    return math.acos(x)

@mcp.tool()
def atan(x: float) -> float:
    """calculate the arctangent of a value"""
    return math.atan(x)

@mcp.tool()
def sinh(x: float) -> float:
    """calculate the hyperbolic sine of a value"""
    return math.sinh(x)

@mcp.tool()
def cosh(x: float) -> float:
    """calculate the hyperbolic cosine of a value"""
    return math.cosh(x)

@mcp.tool()
def tanh(x: float) -> float:
    """calculate the hyperbolic tangent of a value"""
    return math.tanh(x)

@mcp.tool()
def asinh(x: float) -> float:
    """calculate the inverse hyperbolic sine of a value"""
    return math.asinh(x)

@mcp.tool()
def acosh(x: float) -> float:
    """calculate the inverse hyperbolic cosine of a value"""
    if x < 1:
        raise ValueError("Input must be greater than or equal to 1.")
    return math.acosh(x)

@mcp.tool()
def atanh(x: float) -> float:
    """calculate the inverse hyperbolic tangent of a value"""
    if x <= -1 or x >= 1:
        raise ValueError("Input must be in the range (-1, 1).")
    return math.atanh(x)
@mcp.tool()
def exp(x: float) -> float:
    """calculate the exponential of a value"""
    return math.exp(x)

@mcp.tool()
def log10(x: float) -> float:
    """calculate the base-10 logarithm of a value"""
    if x <= 0:
        raise ValueError("Logarithm is not defined for non-positive numbers.")
    return math.log10(x)

@mcp.tool()
def log2(x: float) -> float:
    """calculate the base-2 logarithm of a value"""
    if x <= 0:
        raise ValueError("Logarithm is not defined for non-positive numbers.")
    return math.log2(x)

@mcp.tool()
def ceil(x: float) -> int:
    """calculate the ceiling of a value"""
    return math.ceil(x)

@mcp.tool()
def floor(x: float) -> int:
    """calculate the floor of a value"""
    return math.floor(x)

@mcp.tool()
def round_number(x: float, ndigits: int = 0) -> float:
    """round a number to a given number of decimal places"""
    return round(x, ndigits)

@mcp.tool()
def abs_value(x: float) -> float:
    """calculate the absolute value of a number"""
    return abs(x)

@mcp.tool()
def max_value(*args: float) -> float:
    """find the maximum value among the given numbers"""
    return max(args)

@mcp.tool()
def min_value(*args: float) -> float:
    """find the minimum value among the given numbers"""
    return min(args)

@mcp.tool()
def average(*args: float) -> float:
    """calculate the average of the given numbers"""
    if not args:
        raise ValueError("At least one number is required.")
    return sum(args) / len(args)

@mcp.tool()
def median(*args: float) -> float:
    """calculate the median of the given numbers"""
    if not args:
        raise ValueError("At least one number is required.")
    sorted_args = sorted(args)
    n = len(sorted_args)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_args[mid - 1] + sorted_args[mid]) / 2
    else:
        return sorted_args[mid]

@mcp.tool()
def mode(*args: float) -> float:
    """calculate the mode of the given numbers"""
    if not args:
        raise ValueError("At least one number is required.")
    frequency = {}
    for num in args:
        frequency[num] = frequency.get(num, 0) + 1
    max_freq = max(frequency.values())
    modes = [num for num, freq in frequency.items() if freq == max_freq]
    return modes[0] if len(modes) == 1 else modes

@mcp.tool()
def variance(*args: float) -> float:
    """calculate the variance of the given numbers"""
    if not args:
        raise ValueError("At least one number is required.")
    mean = sum(args) / len(args)
    return sum((x - mean) ** 2 for x in args) / len(args)

@mcp.tool()
def standard_deviation(*args: float) -> float:
    """calculate the standard deviation of the given numbers"""
    if not args:
        raise ValueError("At least one number is required.")
    variance_value = variance(*args)
    return variance_value ** 0.5

@mcp.tool()
def correlation(x: list[float], y: list[float]) -> float:
    """calculate the correlation coefficient between two lists of numbers"""
    if len(x) != len(y):
        raise ValueError("Lists must have the same length.")
    n = len(x)
    if n == 0:
        raise ValueError("Lists must not be empty.")
    mean_x = sum(x) / n
    mean_y = sum(y) / n
    numerator = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(n))
    denominator = (sum((x[i] - mean_x) ** 2 for i in range(n)) * sum((y[i] - mean_y) ** 2 for i in range(n))) ** 0.5
    if denominator == 0:
        raise ValueError("Correlation is undefined for constant lists.")
    return numerator / denominator


@mcp.tool()
def regression(x: list[float], y: list[float]) -> tuple[float, float]:
    """calculate the linear regression coefficients (slope and intercept) for two lists of numbers"""
    if len(x) != len(y):
        raise ValueError("Lists must have the same length.")
    n = len(x)
    if n == 0:
        raise ValueError("Lists must not be empty.")
    mean_x = sum(x) / n
    mean_y = sum(y) / n
    numerator = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(n))
    denominator = sum((x[i] - mean_x) ** 2 for i in range(n))
    if denominator == 0:
        raise ValueError("Regression is undefined for constant x values.")
    slope = numerator / denominator
    intercept = mean_y - slope * mean_x
    return slope, intercept

@mcp.tool()
def integrate(f: callable, a: float, b: float, n: int = 1000) -> float:
    """calculate the definite integral of a function f from a to b using the trapezoidal rule"""
    if n <= 0:
        raise ValueError("Number of intervals must be positive.")
    h = (b - a) / n
    integral = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        integral += f(a + i * h)
    return integral * h

@mcp.tool()
def differentiate(f: callable, x: float, h: float = 1e-5) -> float:
    """calculate the derivative of a function f at a point x using the central difference method"""
    return (f(x + h) - f(x - h)) / (2 * h)

@mcp.tool()
def limit(f: callable, x: float, h: float = 1e-5) -> float:
    """calculate the limit of a function f as x approaches a point"""
    return f(x + h)

@mcp.tool()
def series_expansion(f: callable, x: float, n: int = 10) -> float:
    """calculate the Taylor series expansion of a function f at a point x up to n terms"""
    result = 0
    for i in range(n):
        result += (f(x) / factorial(i)) * (x ** i)
    return result

@mcp.tool()
def series_convergence(f: callable, x: float, n: int = 10) -> bool:
    """check if the Taylor series expansion of a function f converges at a point x"""
    return abs(f(x)) < 1e-5

@mcp.tool()
def series_divergence(f: callable, x: float, n: int = 10) -> bool:
    """check if the Taylor series expansion of a function f diverges at a point x"""
    return abs(f(x)) >= 1e-5

@mcp.tool()
def series_radius_of_convergence(f: callable, x: float, n: int = 10) -> float:
    """calculate the radius of convergence of the Taylor series expansion of a function f at a point x"""
    return 1 / max(abs(f(x + i)) for i in range(n))


if __name__ == "__main__":
    # Run the server
    mcp.run(transport='stdio')